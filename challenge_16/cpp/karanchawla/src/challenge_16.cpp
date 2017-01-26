//
// Created by karan on 1/24/17.
//

//Just basic implementation of permutation formula
#include "challenge_16.h"
#include <string>

// Iterates through the string to calculate the factorial
int challenge_16::calculatePermutations(std::string &str)
{
    std::string::size_type length = str.size();
    int fact = 1;
    for(int i=length; i>0; i--)
    {
        fact = fact*i;
    }
    return fact;
}

