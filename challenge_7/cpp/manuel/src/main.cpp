#include <iostream>
#include <string>
#include <vector>

#include "include/tools.h"

int main(int argc, char **argv) {

    std::string input; // stores string input
    std::getline(std::cin, input); // get line from standard input

    // Convert string of numbers to array of numbers
    std::vector<int> numbers = tools::string_to_numbers(input);

    int length = numbers.size();

    int missing_number = tools::sum_of_n(length);

    // Subtracting values until we get missing number
    for(auto i: numbers) {
        missing_number -= i;
    }

    std::cout << missing_number << std::endl;

    return 0;
}
