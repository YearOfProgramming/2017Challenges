#include <stdio.h>	/* standard i/o lib */

#define STCKSIZE 128	/* size of character stack */

int main(){

	int c, stck[STCKSIZE];	/* vars for current character and stack */
	int i = 0;		/* used to increment stack */

	printf("Type the input you want to reverse then type ctrl+d (EOF character).\n");

	while((c = getchar()) != EOF){	/* wait for ctrl+d (EOF) */
		stck[i] = c;		/* add character to stack */
		i++;			/* increment stack */
	}

	while(i >= 0){			/* iterate back through stack */
		putchar(stck[i]);
		i--;			/* decrement */
	}

	printf("\n");	/* print final endline */
	return 0;
}
