#include <iostream>
#include <string>
#include <vector>
#include "include/majorityElement.h"

int main(int argc, char **argv) {

    std::string input; // will contain a string of numbers

    std::vector<int> numbers;

    std::getline(std::cin, input);

    // Array of numbers
    numbers = stringToDigits(input);
    int length = numbers.size();

    //max value in array
    int max = findMax(numbers);

    // count array to determine majority element
    int *count = new int[max + 1]();

    for(int i = 0; i < length; i++) {
        count[numbers[i]] += 1;
    }

    for(int i = 0; i <= max; i++) {
        if( count[i] > length/2) {
            std::cout << i << std::endl;
            break;
        }
    }

    delete[] count;

    return 0;
}
