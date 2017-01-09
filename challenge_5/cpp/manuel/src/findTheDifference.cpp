#include <limits.h> // For INT_Min
#include <string>
#include "findTheDifference.h"

int findMax (std::string str) {

    int max = INT_MIN;

    for(int i = 0; i < str.length(); i++) {
        if(str[i] > max) {
            max = str[i];
        }
    }

    return max;
}

