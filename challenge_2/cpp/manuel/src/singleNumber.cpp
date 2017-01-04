#include <limits.h> // For INT_Min
#include <string>
#include <sstream>
#include <vector>
#include <math.h>
#include "singleNumber.h"

int findMax (std::vector<int> arr) {

    int max = INT_MIN;

    for(int i = 0; i < arr.size(); i++) {
        if(arr[i] > max) {
            max = arr[i];
        }
    }

    return max;
}

std::vector<int> stringToDigits (std::string stringDigits) {
    // Converts a string of digits (e.g. "2,0,2,3,4") to a array of integers

    std::vector<int> numbers;

    std::stringstream ss(stringDigits);

    int digit;
    // while each character is insert as a digit from the string
    while(ss >> digit) {
        numbers.push_back(digit);

        if(ss.peek() == ',') {
            ss.ignore();
        }
    }

    return numbers;
}
