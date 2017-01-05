#include <iostream>
#include <string>

int main() {
    std::string input;
    std::cin >> input;
    
    for(int i = 1; i <= input.length(); i++) {
        std::cout << input[input.length()-i];
    }
    std::cout << std::endl;
    
    return 0;
}
