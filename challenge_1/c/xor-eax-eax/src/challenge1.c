#include <stdio.h>
#include <stdlib.h>
#include <string.h> // for memset

int main()
{
    // Initialize a character array with the string you want to reverse.
    char helloString[] = "Hello";
    // Get length of 0-indexed string, this will be used for index looping
    int strSize = strlen(helloString);
    // Instantiated character array equal to the size of the original
    char revHelloStr[strSize];
    // Set the values of the reverse character array to zero, this takes care of the null terminator at the end
    memset(revHelloStr, 0, strSize*sizeof(char));
    // subtracted one to disclude the null terminator.  That is taken care of in revHelloStr by the memset
    int i = strSize-1;
    int j = 0;
    // Perform a count from the front to back of the character array for the reverse string
    // while counting from the back of the hello string, skipping the null terminator
    for (i,j ; i>=0 && j<=strSize-1 ; i--, j++)
    {
        revHelloStr[j] = helloString[i];

    }
    printf("%s",revHelloStr);

    return 0;
}
