#include <iostream>
#include <string>
#include <map>

#include "include/tools.h"

int main(int argc, char **argv) {

    std::string input;
    std::getline(std::cin, input);

    std::map<char, int> counter = tools::count(input);
    if (tools::verify_closers(counter)) {
        std::cout << "True" << std::endl;
    } else {
        std::cout << "False" << std::endl;
    }

    return 0;
}
