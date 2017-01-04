#include <iostream>
#include <string.h>


// Prototypes
std::string reverseString(std::string myString);
void swap(char &a, char &b);

int main(int argc, char* argv[]) {

    // define our input string
    std::string inputString;

    // use stdin to grab our string
    // *Note using getline will allow us to grab a full sentence
    std::getline(std::cin, inputString);
    //output our reversal
    std::cout << reverseString(inputString) << '\n';

    return 0;
}

//swap function by reference
void swap(char &a, char &b) {
    char tmp = a;
    a = b;
    b = tmp;
}

std::string reverseString(std::string inputStr) {
    //Grab length
    unsigned int inputStrLen = inputStr.length();

    //Iterate over half of the length
    for(int i=0; i < inputStrLen/2; i++) {
        //swap first and last and loop
        swap(inputStr[i], inputStr[inputStrLen-1-i]);
    }

    return inputStr;
}
