#include <string>
#include <vector>
#include <sstream>

#include "include/tools.h"

namespace tools {

    std::vector<int> string_to_numbers (std::string str) {
        // Given a string "1,2,3,4,5" this outputs
        // an array of integers [1,2,3,4,5]

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

    int sum_of_n(int N) {
        // N + (N- 1) + (N - 2) + ... + (N - N)

        return N * (N + 1) / 2;
    }

}
            

