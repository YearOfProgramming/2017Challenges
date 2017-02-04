#include <stdio.h>
 
int paths(int m, int n) {
	int p;
	if (m==1 || n==1) {
		return 1;
	}
	p = ( paths(m-1,n) + paths(m,n-1) );
	return p;
}

int main () {

   int n, ans, i;
   char choice='Y';
	
	printf("\nThis program determines the number of possible paths to traverse a matrix.");	
	printf("\n____________________________________________________________________________\n");
	printf("\n   We are going to do this assuming,");
	printf("\na. The coordinates begin at the bottom left of the matrix (0,0)");
	printf("\nb. The coordinates end at the top right of the matrix (n,n).\n\n");
	printf("This program will find all possible paths through the matrix,");
	printf("\nconsidering you may only move up or to the right.\n\n");
	printf("The program will take one arguement from standard input,");
	printf("\nthe size of the matrix.\n\n");
	printf("This will be a single number that will denote a n x n matrix.\n\n");
	printf("A program like this will have an enormous time complexity so please don't try matrices larger than N = 15.\n\n");
	printf("            Let's start!!!");
	
	while (choice == 'Y'||choice == 'y'){
	
		printf("\n____________________________________________________________________________\n");
		printf("\n   Enter the size of the Matrix: ");
		scanf("%d", &n);
		//Provision to skip the calculation if size more than threshold value of 15, as stated in the problem.
		while (n > 15)
		{goto end;}
		ans=paths(n,n);
		printf("   Possible Paths : %d\n", ans);
		ans=1;
	
		printf("   Would you like to calculate the paths again?\n   Enter Y or N: ");
		scanf(" %c", &choice);
	}
	end:
	printf("\n____________________________________________________________________________\n");
	printf("\n   This program was brought to you by Your Pal Nurav.\n\n               GoodBye!\n");
	printf("\n____________________________________________________________________________\n\n\n\n");
		return 0;
}
