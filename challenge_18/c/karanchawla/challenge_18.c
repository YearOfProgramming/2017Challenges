//Karan Chawla
//Challenge 18 

#include <stdio.h> 
#include <stdlib.h> 

//recursively add the paths from each possible scenario
//until the dimenion of either dimension is reduced to 1
int numberofPaths(int n, int m)
{
	if(n==1 || m==1)
		return 1;

	return numberofPaths(n-1,m) + numberofPaths(n,m-1);
}

//Driver function
int main(void)
{
	int n;
	scanf("%d", &n);

	printf("%d\n", numberofPaths(n,n));

}