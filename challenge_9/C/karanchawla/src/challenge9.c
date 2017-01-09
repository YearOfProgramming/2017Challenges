/*
Author: karanchawla
Challenge 9
Sort in O(n) after you've squared each element in the given array. 
Used Counting Sort as its running time is O(n)
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h> 

//determines the maximum number of digits that can be sorted with this method. 
//Change MAX if your number of digits is different
#ifndef MAX
#define MAX 1000000
#endif

//utility function to print array
void printArray(int *a, int size)
{
    for(int i=0;i<size;i++) printf("%d ",a[i]);
}

//Counting sort implementation
//Copy the output array to original array
//if you want to further process the output
void countingSort(int *a,int size)
{
    int output[size];
    memset(output,0,size);

    int count[MAX];
    for(int i=0;i<MAX;i++) count[i] = 0;
    
    for(int i=0;i<size;i++)
    {
        count[a[i]]++;
    }

    for(int i=1;i<MAX;i++)
        count[i] += count[i-1];

    for(int i=size-1;i>=0;i--)
    {
        output[count[a[i]]-1] = a[i];
        count[a[i]]--;
    }

    printArray(output,size);
    printf("\n");
}

//utility function to square the array
void square(int *a, int size)
{
    for(int i=0;i<size;i++) a[i] = a[i]*a[i];
}

//Driver program 
int main(void)
{
    //Example 1
    int a[] = {-5,-4,-3,-2};
    int size = sizeof(a)/sizeof(*a);

    //Example 2
    int b[] = {-2,-1,0,1,2};
    int n = sizeof(b)/sizeof(*b);

    square(a,size);
    square(b,n);

    countingSort(a,size);
    countingSort(b,n);

    return 0;
}