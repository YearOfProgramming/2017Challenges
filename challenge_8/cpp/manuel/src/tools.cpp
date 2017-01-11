#include <string>
#include <vector>
#include <sstream>

#include "include/tools.h"

namespace tools {

    std::vector<int> string_to_numbers (std::string str) {

        std::vector<int> numbers;
        std::stringstream ss(str);
        int number;

        while ( ss >> number ) {
            numbers.push_back(number);

            if(ss.peek() == ',') {
                ss.ignore();
            }
        }

        return numbers;
    }

}
            

