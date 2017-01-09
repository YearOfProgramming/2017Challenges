/*
Karan Chawla
Challenge #3
Algorithm: Moore's voting algorithm
Time Complexity: O(n)
Auxillary Space: O(1)
*/

#include <stdio.h> 
#include <stdlib.h>

//find majority candidate in an array
int findCandidate(int *a, int size)
{
    int majIndex = 0, count = 1;
    int i;
    for (i = 1; i < size; i++)
    {
        if (a[majIndex] == a[i])
            count++;
        else
            count--;
        if (count == 0)
        {
            majIndex = i;
            count = 1;
        }
    } 
    return a[majIndex];
}

//utility function to check if majority candidate occurs > n/2 times
int isMajority(int *a, int size, int candidate)
{
	int i = 0; 
	int count = 0;
	for(int i=0;i<size;i++)
	{
		if(a[i]==candidate)
		{
			count++;
		}
	}
	if(count>size/2) return 1;
	
	else return 0;
}


void printMajority(int a[], int size)
{
  int cand = findCandidate(a, size);
 
  if (isMajority(a, size, cand))
    printf("Majority element: %d", cand);
  else
    printf("No Majority Element");
}

//driver function 
int main(void)
{
	int a[] = {1,3,3,3,2,1,1,3,6,3,3,3,3,3};
	int size = sizeof(a)/sizeof(*a);
	printMajority(a,size);
	return 0;
}