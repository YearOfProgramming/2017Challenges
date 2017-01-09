#include <iostream>
#include <string>
#include <vector>
#include "singleNumber.h"

int main(int argc, char **argv) {

    std::string input; // will contain a string of numbers

    int lines; // the numbers of strings expected as input
    std::cin >> lines;
    std::cin.ignore(); // ignore trailing \n

    std::vector<int> numbers;

    // for every array of integers to check 
    for(int i = 0; i < lines; i++) {

        std::getline(std::cin, input);

        numbers = stringToDigits(input);

        //max value in array
        int max = findMax(numbers);

        // count array to determine single digit
        int *count = new int[max + 1];

        for(int i = 0; i < numbers.size(); i++) {
            count[numbers[i]] += 1;
        }

        int singleDigit = 0;
        while(count[singleDigit] != 1) {
            singleDigit++;
        }

        std::cout << singleDigit << std::endl;

    }
    return 0;
}
