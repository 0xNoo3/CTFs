#include<stdio.h>
#include <string.h>
#include<unistd.h>

__attribute__((constructor))
void __constructor__(){
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

void getmessage(void)
{
    char msg[200];
    printf("Enter the message: ");
    scanf(" %[^\n]s", msg);
    printf("Message received.\n");

}

int main(void)
{
    char name[30];
    printf("Your name: ");
    scanf("%s", name);
    printf("Welcome ");
    printf(name);
    printf("\n");
    getmessage();
    return 0;
}

