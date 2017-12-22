#include <stdio.h>

//paths function that will calculate return the no. of paths to the main function.
int paths(int m, int n){
	int p;
	//Tackles the problem by dividing it into matrices of size=1.
	//As there's just 1 path for a matrix of size 1 this loop is like solving a sub-problem
	if (m==1 || n==1) {
		return 1;
	}
	
	p = ( paths(m-1,n) + paths(m,n-1) );//nesting the paths funtion into itself.
	return p;
}

int main () {

   int n, ans, i;//declaring the variables, n=MatrixSize, ans=FinalNumberOfPaths, i=ForIncrements
   char choice='Y';
	
	//Just displays the problem statement and requirements. This part can be omitted to make the program shorter.
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
		printf("\n   Enter the size of the Matrix: ");//Takes input from the user.
		scanf("%d", &n);
		//Provision to skip the calculation if size more than threshold value of 15, as stated in the problem.
		while (n > 15)
		{goto end;}//cancels the calculation of paths to avoid time complexity.
		ans=paths(n,n);//calls path funtion and assigns the returned value to 'ans' our Answer variable.
		printf("   Possible Paths : %d\n", ans);//Displays the numbers of possible paths for the given matrix size.
		ans=1;//Resets the value of 'ans' to 1 in case user executes this loop again for a different matrix size.
	
		printf("   Would you like to calculate the paths again?\n   Enter Y or N: ");//Provision for User to not break the loop
		scanf(" %c", &choice);//If choice entered is anything other than 'Y' or 'y' the while loop will break.
	}
	end:
	//These comments can be Omitted.
	printf("\n____________________________________________________________________________\n");
	printf("\n   This program was brought to you by Your Pal Nurav.\n\n               GoodBye!\n");
	printf("\n____________________________________________________________________________\n\n\n\n");
		return 0;
}
