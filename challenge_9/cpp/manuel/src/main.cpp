#include <vector>
#include <iostream>
#include <string>
#include <math.h>

#include "include/tools.h"

int main(int argc, char **argv) {

    // Get input
    std::string input;
    // Store string of numbers
    std::getline(std::cin, input);

    // Convert string of numbers to array
    std::vector<int> numbers = tools::string_to_numbers(input);
    // Apply aglorithm
    std::vector<int> sorted = tools::sort_squares(numbers);

    for(auto i: sorted) {
        std::cout << i << std::endl;
    }

    return 0;
}


