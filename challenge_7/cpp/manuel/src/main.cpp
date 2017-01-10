#include <iostream>
#include <string>
#include <vector>

#include "include/tools.h"

int main(int argc, char **argv) {

    std::string input;
    std::getline(std::cin, input);

    std::vector<int> numbers = tools::string_to_numbers(input);

    int length = numbers.size();

    int missing_number = tools::sum_of_n(length);

    for(auto i: numbers) {
        missing_number -= i;
    }

    std::cout << missing_number << std::endl;

    return 0;
}
