#include <iostream>
#include <string>
#include <vector>
#include "include/singleNumber.h"

int main(int argc, char **argv) {

    std::string input; // will contain a string of numbers

    std::vector<int> numbers;


    std::getline(std::cin, input);

    numbers = stringToDigits(input);
    int length = numbers.size();

    //max value in array
    int max = findMax(numbers);

    // count array to determine single digit
    int *count = new int[max + 1]();

    for(int i = 0; i < length; i++) {
        count[numbers[i]] += 1;
    }

    int singleDigit = 0;
    while(count[singleDigit] != 1) {
        singleDigit++;
    }

    std::cout << singleDigit << std::endl;

    return 0;
}
