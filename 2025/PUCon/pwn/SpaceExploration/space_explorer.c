#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define MAX_CARGO 6
#define CARGO_SIZE 64

__attribute__((constructor)) void setup_console()
{
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

char *ship_cargo[MAX_CARGO + 1] = {NULL};
int cargo_status[MAX_CARGO + 1] = {0};

void openCompartment(int index);
void loadCargo(int index, const char *item);
void deployItem(int index, char *anomaly);
void ejectCargo(int index);
void encounterAlien();
void spaceExploration();
void handleAnomaly(char *anomaly);


void openCompartment(int index)
{
    if (ship_cargo[index] == NULL)
    {
        ship_cargo[index] = (char *)malloc(CARGO_SIZE);
        cargo_status[index] = 1;
        if (ship_cargo[index] == NULL)
        {
            printf("<<< Failed to initialize cargo compartment %d!\n", index);
            exit(1);
        }
        printf("<<< Opened cargo compartment %d.\n", index);
    }
}

void loadCargo(int index, const char *item)
{
    if (ship_cargo[index] == NULL)
    {
        printf("<<< Cargo compartment %d is not accessible.\n", index);
    }
    else
    {
        if (cargo_status[index] == 0)
        {
            ship_cargo[index] = malloc(CARGO_SIZE);
        }
        strncpy(ship_cargo[index], item, CARGO_SIZE - 1);
        ship_cargo[index][CARGO_SIZE - 1] = '\0';
        printf("<<< Loaded %s into cargo compartment %d.\n", item, index);
    }
}

void deployItem(int index, char *anomaly)
{
    if (cargo_status[index] == 1)
    {
        printf("<<< Deploying item from compartment %d: %s\n", index, ship_cargo[index]);
        if (strcmp(ship_cargo[index], "Laser Cannon") == 0 && strcmp(anomaly, "asteroid") == 0)
        {
            printf("<<< You blast the asteroid with your Laser Cannon!\n");
        }
        else if (strcmp(ship_cargo[index], "Radiation Shield") == 0 && strcmp(anomaly, "solar flare") == 0)
        {
            printf("<<< You protect yourself from the solar flare with the Radiation Shield!\n");
        }
        else if (strcmp(ship_cargo[index], "Navigation Array") == 0 && strcmp(anomaly, "nebula") == 0)
        {
            printf("<<< You navigate through the nebula with the Navigation Array!\n");
        }
        else if ((strncmp(ship_cargo[index], "Alien", 5) == 0))
        {
            printf("<<< The alien reveals a secret wormhole coordinate: %p\n", &printf);
        }
        else
        {
            printf("<<< The %s isn't effective against the %s.\n", ship_cargo[index], anomaly);
        }
    }
    else
    {
        printf("<<< Compartment %d is empty.", index);
    }
}

void ejectCargo(int index)
{
    if (ship_cargo[index] != NULL && cargo_status[index] == 1)
    {
        free(ship_cargo[index]);
        printf("<<< Ejected cargo from compartment %d.\n", index);
    }
    else
    {
        printf("<<< Compartment %d is already empty.\n", index);
    }
    cargo_status[index] = !cargo_status[index];
}

void handleAnomaly(char *anomaly)
{
    if (strcmp(anomaly, "asteroid") == 0)
    {
        printf("<<< A massive asteroid is on collision course with your ship!\n");
    }
    else if (strcmp(anomaly, "solar flare") == 0)
    {
        printf("<<< Warning: Dangerous solar flare detected in proximity!\n");
    }
    else if (strcmp(anomaly, "nebula") == 0)
    {
        printf("<<< Your ship is caught in a disorienting nebula cloud.\n");
    }
    else if (strcmp(anomaly, "black hole") == 0)
    {
        printf("<<< A black hole is generating intense gravitational pull nearby!\n");
    }
    else if (strcmp(anomaly, "ancient artifact") == 0)
    {
        printf("<<< You detect an ancient alien artifact floating in space! Perhaps something special can unlock its secrets.\n");
    }
}

void __attribute__((stack_protect)) spaceExploration()
{
    int choice, compartment;
    char *items[] = {"Laser Cannon", "Radiation Shield", "Navigation Array", "Oxygen Supply", "Emergency Rations", "Fusion Torch"};
    char *anomalies[] = {"asteroid", "solar flare", "nebula", "black hole", "ancient artifact", "nothing"};

    srand(time(0));
    printf("Welcome to the Space Exploration Mission!\n");

    for (int i = 1; i < 7; i++)
    {
        openCompartment(i);
        loadCargo(i, items[i - 1]);
    }

    for (int mission_day = 1; mission_day <= 25; mission_day++)
    {
        printf("\n=== Mission Day %d ===\n", mission_day);
        int anomalyIndex = rand() % 5;
        handleAnomaly(anomalies[anomalyIndex]);

        printf("\n=== Select Operation ===\n");
        printf("1. Deploy equipment\n2. Load new cargo\n3. Eject cargo\n");
        printf("Enter your selection >>> ");
        scanf("%d", &choice);
        getchar();

        switch (choice)
        {
        case 1:
            printf("Deploy from which compartment (1-6) >>> ");
            scanf("%d", &compartment);
            getchar();
            if (compartment >= 1 && compartment <= 6)
                deployItem(compartment, anomalies[anomalyIndex]);
            else
                printf("<<< Invalid compartment number.\n");
            break;
        case 2:
            printf("Select a compartment to load new cargo (1-6) >>> ");
            scanf("%d", &compartment);
            getchar();
            if (compartment >= 1 && compartment <= 6)
            {
                printf("Enter cargo designation >>> ");

                if (cargo_status[compartment] == 0)
                {
                    ship_cargo[compartment] = malloc(CARGO_SIZE);
                    cargo_status[compartment] = 1;
                }

                char *ptr = ship_cargo[compartment];
                memset(ptr, 0, 24);
                read(0, ptr, CARGO_SIZE);
            }
            else
            {
                printf("<<< Invalid compartment number.\n");
            }
            break;
        case 3:
            printf("Select a compartment to eject cargo (1-6) >>> ");
            scanf("%d", &compartment);
            getchar();
            if (compartment >= 1 && compartment <= 6)
                ejectCargo(compartment);
            else
                printf("<<< Invalid compartment number.\n");
            break;
        default:
            printf("<<< Invalid selection.\n");
        }
    }
}

int main()
{
    spaceExploration();
    return 0;
}