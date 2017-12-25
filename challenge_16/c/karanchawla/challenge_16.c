//Karan Chawla
//Challenge 16
//Also allows for repeated characters in the input string

#include <stdio.h> 
#include <stdlib.h>
#include <string.h>

//function to return counts of each character in the string
void getCounts(const char *str, int *counts, size_t size)
{
	for (int i=0; i<size; i++)
	{
		counts[str[i]]++;
	}

}

//returns factorial of each number
int getFactorial(int x)
{
	int fact = 1;
	for (int i = 1; i <=x; ++i)
	{
		fact *= i;
		/* code */
	}
	return fact;
}

//returns factorial of string if all chars unique
int stringfactorial(const char* str, size_t size)
{
	int fact = 1;
	for(int i=1; i<=size-1; i++)
	{
		fact *= i;
	}

	return fact;
}

//returns total permutations
int getPermutations(const char *str, int *counts, size_t size)
{
	int fact = stringfactorial(str,size);
	getCounts(str,counts,size);
	for (int i = 0; i < 256; ++i)
	{	
		if(counts[i]>1)
		{
			fact = fact/getFactorial(counts[i]);
		}
	}

	return fact;

}

//utility function to print array/string
void printArray(int *a, size_t size)
{	
	for (int i = 0; i < size; ++i)
	{
		printf("%d ", *(a+i));
	}

}


//driver program
int main(void)
{
	char str[] = "abbcd3";
	size_t size = sizeof(str)/sizeof(*str);
	int counts[256] = {0};
	printf("%d\n", getPermutations(str,counts,size)); //should print 6!/2! = 360
	
	return 0;
}