#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <math.h>

#include "include/tools.h"

std::vector<int> tools::string_to_numbers(std::string input) {
    // Given a string "1,2,3,4,5" this outputs
    // an array of integers [1,2,3,4,5]
    std::stringstream ss(input);
    std::vector<int> numbers;
    int number;

    while(ss >> number) {
        numbers.push_back(number);

        if(ss.peek() == ',') {
            ss.ignore();
        }
    }

    return numbers;
}

std::vector<int> tools::sort_squares(std::vector<int> numbers) {
    // Will square the values of a sorted array and resport in O(N)
    int length = numbers.size();

    std::vector<int> sorted;
    int left_length = 0;
    int right_length = length;

    // Square left side values of array first
    for(int i = 0; numbers[i] < 0; i++) {
        left_length++;
        right_length--;

        numbers[i] = pow(numbers[i], 2);
    }

    int left_index = left_length - 1;
    int right_index = left_length;
    bool squared = false; // Checks if this value has been squared

    // Compare both sides of array and insert accordingly
    while(right_length > 0 && left_length > 0) {

        // Cotntinue squaring only if right index increments
        if(!squared) {
            numbers[right_index] = pow(numbers[right_index], 2); // continue squaring
            squared = true;
        }

        // If next right index is smaller insert, otherwise
        // insert the left one
        if(numbers[right_index] <= numbers[left_index]) {
            sorted.push_back(numbers[right_index]);
            right_index++;
            right_length--;
            squared = false;
        } else {
            sorted.push_back(numbers[left_index]);
            left_index--;
            left_length--;
        }
    }

    // Simply insert the last numbers of the longer side of the array
    
    // If the right array was longer, then insert the rest in order
    while(right_length > 0) {
        numbers[right_index] = pow(numbers[right_index], 2);
        sorted.push_back(numbers[right_index]);
        right_index++;
        right_length--;
    }

    // If the left  array was longer, then insert the rest in order
    while(left_length > 0 ) {
        sorted.push_back(numbers[left_index]);
        left_index--;
        left_length--;
    }

    return sorted;
}


