#include <vector>
#include <iostream>
#include <string>
#include <math.h>

#include "include/tools.h"

int main(int argc, char **argv) {

    // Get input
    std::string input;
    std::getline(std::cin, input);

    std::vector<int> numbers = tools::string_to_numbers(input);
    std::vector<int> sorted = tools::sort_squares(numbers);

    for(auto i: sorted) {
        std::cout << i << std::endl;
    }

    return 0;
}


