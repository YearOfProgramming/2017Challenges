/*
For this coding challenge you are given an array of random integers where every
integer is repeated except for a single one. Your challenge is to find the single
integer that does NOT repeat.

example: given array = [2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7]
your program should return: 5
*/
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int array[] = {2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7};
    int sz = sizeof(array)/sizeof(array[0]) - 1; // 0 - 17 = 18 elements
    int i = 0; // outside for loop counter
    int j = 0; // inside for loop counter
    int currentIndex = 0; // the value from the array that is being compared to the rest of the array in a loop
    int singleInstance = 0; // will be incremented when a currentIndex doesn't have an instanceCounter greater than 0, it is unique
    int instanceCounter; // will keep track of multiple occurences of an array number

    // Start first loop, the element will be stored in currentIndex to be compared to the other array elements in the inner loop
    for(i ; i<=sz ; i++)
    {
        currentIndex = array[i];
        // instanceCounter and j must be reset between runs of the inner for loop or they will continue to increment
        instanceCounter = 0;
        j = 0;

        // inner loop checks current array index against other array indecies.  If duplicates aren't found, that index is the only one
        for(j ; j<=sz ; j++)
        {
            // don't compare against yourself
            if(j==i)
            {
                continue;
            }

            // If the value that entered this loop is elsewhere, add to instance counter
            if(currentIndex == array[j])
            {
                instanceCounter+=1;
            }

            // If you made it to the end and the instance counter hasen't incremented, that is the only instance
            if((j==sz) && (instanceCounter==0))
            {
                singleInstance = currentIndex;
            }
            else
            {
                continue;
            }

        } // end j loop
    } // end i loop

    printf("%d", singleInstance);

    return 0;
}
