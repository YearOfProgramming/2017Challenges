/*
Karan Chawla
Missing Number
*/

#include "stdio.h"

// Calculates the sum of all numbers upto n and subtracts each array element. 
// Returns the thus obtained value. 
int missingNumber(int*a, int size)
{
	
	int total = (size)*(size+1)/2;
	for(int i=0;i<size;i++)
	{
		total = total - a[i];
	}

	return total;
}

//driver program
int main(void)
{
	//Example 1
	//int a[] = {0,1,2,4};
	
	//Example 2
	int a[] = {1,2,3};
	int size = sizeof(a)/sizeof(*a);
	printf("The missing number is: %d\n", missingNumber(a,size));

	return 0;
}