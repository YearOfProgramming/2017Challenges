#include <stdio.h>
#include <string.h>


// Function that will search for the majority int, if there is one
int findMajorityInt(int arr[], int arrSz)
{
    int i = 0;
    int currentNum;
    int j;
    int majorityNum = 0;
    int numCount;
    // Outside for loop goes through the array and keeps a copy of the current index value
    // Inner for loop counts instances of that value and checks if if occcurs more than
    // n/2 times where n is the number of elements in the array
    for (i; i<arrSz; i++)
    {
        currentNum = arr[i];
        numCount = 0;
        j = 0;
        //printf("\n----OUTERLOOP: %d", currentNum);
        for(j; j<arrSz; j++)
        {
            if(arr[j]==currentNum)
            {
                numCount++;
                //printf("\nNUM COUNT: %d", numCount);
            }

            if(j == arrSz-1 && numCount > (arrSz/2))
            {
                majorityNum = currentNum;
                //printf("\nMAJORITY NUMBER: %d", majorityNum);
                break;
            }

        } // end inner loop

    } //  end outer loop

    return majorityNum;
}



int main( int argc, const char**argv )
{
    char *input = argv[1];

    if( argc == 2 ) // make sure there's only argc and argv
    {
        char *token; // token is used to keep each subsection of the string input
        token = strtok(input, ","); // strtok separates each string input by a delimiting value, in this case a comma
        int inLen = 0; // will keep track of how many entries there are in the user input to limit searching through the loop later
        int initArr[100]; // 100 is arbitrarily sized, if infinitely sized, need to do some pointer business
        while(token != NULL)
        {
            initArr[inLen] = atoi(token); // comes in as a string, need to convert to an integer
            token = strtok (NULL, ","); // part of the nomral functionality of strtok, check man page for details
            inLen++;
            // prevent from running off the buffer, prog description doesn't call for infinite loop
            if (inLen > 99)
            {
                break;
            }
        }
        int majorityInt = 0;
        majorityInt = findMajorityInt(initArr, inLen);
        printf("%d", majorityInt);
    }
    else if( argc > 2 ) // if any space delimited text is passed in, too many args.
    {
        printf("Too many arguments supplied.\n");
    }
    else // if any other case, print out that only one arg is expected
    {
        printf("One argument expected.\n");
    }

    return 0;
}

