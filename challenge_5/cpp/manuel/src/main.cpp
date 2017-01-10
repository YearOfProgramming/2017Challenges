#include <iostream>
#include <string>
#include "include/findTheDifference.h"

int main(int argc, char **argv) {

    std::string s, t;
    std::getline(std::cin, s);
    std::getline(std::cin, t);
    int sLength = s.length();
    int tLength = t.length();

    //max value in array
    int maxS = findMax(s);
    int maxT = findMax(t);

    // count array to determine single digit
    int *countS = new int[maxS + 1]();
    int *countT = new int[maxT + 1]();

    // count the characters
    for(int i = 0; i < sLength; i++) {
        countS[(int)s[i]]++;
    }

    for(int i = 0; i < tLength; i++) {
        countT[(int)t[i]]++;
    }

    // Compare count array for mismatched value
    int differentChar = 'a';
    while(countS[differentChar] == countT[differentChar]) {
        differentChar++;
    }

    // If all of the characters of string s
    // match with string t, then the different character
    // is the largest character of string t
    if(differentChar - 1 == maxS) {
        differentChar = maxT;
    } 

    std::cout << (char)differentChar << std::endl;

    delete[] countS;
    delete[] countT;
    return 0;
}
