#include <iostream>
#include <string>
#include <vector>

#include "include/tools.h"
#include "include/ranges.h"

int main(int argc, char **argv) {

    // Grab line of input
    std::string input;
    std::getline(std::cin, input);

    std::vector<int> numbers = tools::string_to_numbers(input);

    std::vector<std::string> ranges = ranges::get_ranges(numbers);

    for (auto str : ranges) {
        std::cout << str << std::endl;
    }

    return 0;
}
