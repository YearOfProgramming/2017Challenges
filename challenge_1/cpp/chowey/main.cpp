#include <iostream>
#include <string>

int main() {
    std::string input;
    std::cout << "Enter a string to be reversed:" << std::endl;
    std::getline(std::cin,input);
    
    int length = input.length();
    
    for(int i = 1; i <= length; i++) {
        std::cout << input[length-i];
    }
    std::cout << std::endl;
    
    return 0;
}
