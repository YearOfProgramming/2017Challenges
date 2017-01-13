#include <stdio.h>
#include <stdlib.h>
 
/* prototype for asm function */
extern int check_brackets(char input[]);
 
int main()
{
	//Remember that for C: False = 0, True =/= 0
	char* inputbuf;
	int check = 0;
	while(1)
	{
		inputbuf = calloc(1024,sizeof(char));
		printf("Input: ");
		fgets(inputbuf,1024,stdin);
		check = check_brackets(inputbuf);
		printf("%d\n",check);
		free(inputbuf);
	}
	return 0;
}