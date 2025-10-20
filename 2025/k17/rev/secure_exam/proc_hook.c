#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dlfcn.h>
#include <dirent.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>

// Function pointers for original functions
static DIR* (*real_opendir)(const char *name) = NULL;
static struct dirent* (*real_readdir)(DIR *dirp) = NULL;
static int (*real_open)(const char *pathname, int flags, ...) = NULL;
static int (*real_openat)(int dirfd, const char *pathname, int flags, ...) = NULL;
static int (*real_stat)(const char *pathname, struct stat *statbuf) = NULL;
static int (*real_lstat)(const char *pathname, struct stat *statbuf) = NULL;
static int (*real_access)(const char *pathname, int mode) = NULL;

// Initialize function pointers
void init_hooks() {
    if (!real_opendir) {
        real_opendir = dlsym(RTLD_NEXT, "opendir");
    }
    if (!real_readdir) {
        real_readdir = dlsym(RTLD_NEXT, "readdir");
    }
    if (!real_open) {
        real_open = dlsym(RTLD_NEXT, "open");
    }
    if (!real_openat) {
        real_openat = dlsym(RTLD_NEXT, "openat");
    }
    if (!real_stat) {
        real_stat = dlsym(RTLD_NEXT, "stat");
    }
    if (!real_lstat) {
        real_lstat = dlsym(RTLD_NEXT, "lstat");
    }
    if (!real_access) {
        real_access = dlsym(RTLD_NEXT, "access");
    }
}

// Custom directory entry structure for /proc
static struct dirent fake_entries[3];
static int entry_index = 0;
static int is_proc_dir = 0;
static int initialized = 0;
static char current_pid_str[16];

void setup_fake_entries() {
    if (initialized) return;
    
    // Entry 0: "1" (init)
    fake_entries[0].d_ino = 1;
    fake_entries[0].d_type = DT_DIR;
    strcpy(fake_entries[0].d_name, "1");
    fake_entries[0].d_reclen = sizeof(struct dirent);
    
    // Entry 1: current PID
    snprintf(current_pid_str, sizeof(current_pid_str), "%d", getpid());
    fake_entries[1].d_ino = getpid();
    fake_entries[1].d_type = DT_DIR;
    strcpy(fake_entries[1].d_name, current_pid_str);
    fake_entries[1].d_reclen = sizeof(struct dirent);
    
    // Entry 2: NULL terminator (not used, just safety)
    memset(&fake_entries[2], 0, sizeof(struct dirent));
    
    initialized = 1;
    fprintf(stderr, "[HOOK] Setup fake /proc with PIDs: 1, %s\n", current_pid_str);
}

DIR* opendir(const char *name) {
    init_hooks();
    
    // Check if opening /proc directory
    if (name && strcmp(name, "/proc") == 0) {
        setup_fake_entries();
        is_proc_dir = 1;
        entry_index = 0;
        
        fprintf(stderr, "[HOOK] Intercepted opendir(/proc)\n");
        return (DIR*)0xdeadbeef;  // Return fake DIR pointer
    }
    
    return real_opendir(name);
}

struct dirent* readdir(DIR *dirp) {
    init_hooks();
    
    // If this is our fake /proc directory
    if (dirp == (DIR*)0xdeadbeef) {
        if (entry_index < 2) {
            fprintf(stderr, "[HOOK] Returning /proc entry: %s\n", fake_entries[entry_index].d_name);
            return &fake_entries[entry_index++];
        } else {
            fprintf(stderr, "[HOOK] End of fake /proc\n");
            return NULL;  // End of directory
        }
    }
    
    return real_readdir(dirp);
}

int closedir(DIR *dirp) {
    static int (*real_closedir)(DIR *dirp) = NULL;
    
    if (!real_closedir) {
        real_closedir = dlsym(RTLD_NEXT, "closedir");
    }
    
    if (dirp == (DIR*)0xdeadbeef) {
        fprintf(stderr, "[HOOK] Closing fake /proc\n");
        is_proc_dir = 0;
        return 0;
    }
    
    return real_closedir(dirp);
}

// Hook stat/lstat for /proc entries
int stat(const char *pathname, struct stat *statbuf) {
    init_hooks();
    
    if (pathname && strncmp(pathname, "/proc/", 6) == 0) {
        const char* pid_part = pathname + 6;
        
        // Only allow our fake PIDs
        if (strcmp(pid_part, "1") == 0 || strcmp(pid_part, current_pid_str) == 0) {
            fprintf(stderr, "[HOOK] stat allowed for %s\n", pathname);
            // Create fake directory stat
            memset(statbuf, 0, sizeof(struct stat));
            statbuf->st_mode = S_IFDIR | 0755;
            statbuf->st_nlink = 2;
            return 0;
        } else {
            fprintf(stderr, "[HOOK] stat blocked for %s\n", pathname);
            errno = ENOENT;
            return -1;
        }
    }
    
    return real_stat(pathname, statbuf);
}

int lstat(const char *pathname, struct stat *statbuf) {
    return stat(pathname, statbuf);  // Same logic
}

// Hook access() calls
int access(const char *pathname, int mode) {
    init_hooks();
    
    if (pathname && strncmp(pathname, "/proc/", 6) == 0) {
        const char* pid_part = pathname + 6;
        
        if (strcmp(pid_part, "1") == 0 || strcmp(pid_part, current_pid_str) == 0) {
            fprintf(stderr, "[HOOK] access allowed for %s\n", pathname);
            return 0;  // Exists and accessible
        } else {
            fprintf(stderr, "[HOOK] access blocked for %s\n", pathname);
            errno = ENOENT;
            return -1;
        }
    }
    
    return real_access(pathname, mode);
}