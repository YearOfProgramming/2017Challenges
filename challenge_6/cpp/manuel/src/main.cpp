#include <iostream>
#include <string>
#include <vector>

#include "include/tools.h"
#include "include/ranges.h"

int main(int argc, char **argv) {

    // Grab line of input
    std::string input;
    // Store string of number
    std::getline(std::cin, input);

    // Convert string of numbers to array of numbers
    std::vector<int> numbers = tools::string_to_numbers(input);

    // Apply algorithm
    std::vector<std::string> ranges = ranges::get_ranges(numbers);

    for (auto str : ranges) {
        std::cout << str << std::endl;
    }

    return 0;
}
