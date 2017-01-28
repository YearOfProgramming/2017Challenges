#include <string>
#include <vector>
#include <sstream>

#include "include/tools.h"

namespace tools {

    std::vector<int> string_to_numbers (std::string str) {
        // Converts an input of numbers as a string to an array of integers
        std::stringstream ss(str);
        std::vector<int> numbers;
        int number;

        while( ss >> number ) {

            numbers.push_back(number);

            if( ss.peek() == ',') {
                ss.ignore();
            }
        }

        return numbers;
    }

}

