#include <iostream>
#include <cstring>
#include <unistd.h>
#include <cstdlib>
#include <limits> 

#define DATA_SIZE 0x1000
char data[DATA_SIZE]; 
void imp(void *address) {
    __asm__ volatile (
        "mov %0, %%rax\n\t"  
        "pop %%rax\n\t"    
        "ret\n\t"           
        :                    
        : "r"(address)       
        : "%rax"             
    );
}

void print_account_statement() {
    char buffer[100];  
    std::cout << "Your account statement:" << std::endl;
    std::cout << "------------------------" << std::endl;
    std::cout << "Account Number: 123456789" << std::endl;
    std::cout << "Balance: $1000" << std::endl;
    std::cout << "Transactions: " << std::endl;
    std::cout << "1. Withdraw: $500" << std::endl;
    std::cout << "2. Deposit: $200" << std::endl;
    std::cout << "3. Withdraw: $300" << std::endl;
    std::cout << "4. Deposit: $100" << std::endl;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::cout << "Enter a message: ";
    std::cin.getline(data, sizeof(data)); 
    if (std::cin.fail()) {
        std::cerr << "Failed to read input!" << std::endl;
        exit(1);
    }
    memcpy(buffer, data, sizeof(buffer)+44);

    std::cout << "Account message: " << buffer << std::endl;
}

void atm_system() {
    int choice;
    
    std::cout << "ATM Menu" << std::endl;
    std::cout << "1. View Account Statement" << std::endl;
    std::cout << "2. Deposit Money" << std::endl;
    std::cout << "3. Withdraw Money" << std::endl;
    std::cout << "Choose an option: ";
    std::cin >> choice;

    switch (choice) {
        case 1:
            print_account_statement();  
            break;
        case 2:
            std::cout << "Depositing money..." << std::endl;
            break;
        case 3:
            std::cout << "Withdrawing money..." << std::endl;
            break;
        default:
            std::cerr << "Invalid choice!" << std::endl;
            break;
    }
}

int main() {
    setvbuf(stdin,0,0,0);
    setvbuf(stdout,0,0,0);

    atm_system();
    return 0;
}
