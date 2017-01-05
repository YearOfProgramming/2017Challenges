#include <iostream>
#include <string>
#include "findTheDifference.h"

int main(int argc, char **argv) {

    std::string s, t;

    int lines; // the numbers of strings expected as input
    std::cin >> lines;
    std::cin.ignore(); // ignore trailing \n

    // for every array of integers to check 
    for(int i = 0; i < lines; i += 2) {

        std::cout << "Testcase: " << i/2 + 1 << std::endl;

        std::getline(std::cin, s);
        std::getline(std::cin, t);

        //max value in array
        int maxS = findMax(s);
        int maxT = findMax(t);

        // count array to determine single digit
        int *countS = new int[maxS + 1]();
        int *countT = new int[maxT + 1]();

        // count the characters
        for(int i = 0; i < s.length(); i++) {
            countS[s[i]]++;
        }

        for(int i = 0; i < t.length(); i++) {
            countT[t[i]]++;
        }

        // Compare count array for mismatched value
        char differentChar = 'a';
        while(countS[differentChar] == countT[differentChar]) {
            differentChar++;
        }

        // If all of the characters of string s
        // match with string t, then the different character
        // is the largest character of string t
        if(differentChar - 1 == maxS) {
            differentChar = maxT;
        } 

        std::cout << differentChar << std::endl;
        
        delete[] countS;
        delete[] countT;
    }
    return 0;
}
