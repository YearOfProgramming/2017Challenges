#include <limits.h> // For INT_Min
#include <string>
#include "include/findTheDifference.h"

int findMax (std::string str) {

    int max = INT_MIN;
    int length = str.length();

    for(int i = 0; i < length; i++) {
        if(str[i] > max) {
            max = str[i];
        }
    }

    return max;
}

