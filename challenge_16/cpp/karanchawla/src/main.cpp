//Karan Chawla
//Challenge 16

#include "challenge_16.h"
#include <iostream>

//Driver program
int main(void)
{
    challenge_16 n;

    std::string test_case1 = "abcde";
    std::string test_case2 = "abc";
    std::string test_case3 = "abcdef";
    std::string test_case4 = "abcdefg";

    std::cout << n.calculatePermutations(test_case1) << std::endl; //should print 120
    std::cout << n.calculatePermutations(test_case2) << std::endl; //should print 6
    std::cout << n.calculatePermutations(test_case3) << std::endl; //should print 720
    std::cout << n.calculatePermutations(test_case4) << std::endl; //should print 5040

    return 0;
}
