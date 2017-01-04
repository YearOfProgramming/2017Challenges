#include <stdio.h>
#include <string.h>

main(int argc, char *argv[]){
    if (argc != 2){
        printf("Improper Arguments\n");
    }
    else{
        int len = strlen(argv[1]);
        int i;
        for (i = len-1; i >= 0; i --){
            printf("%c", argv[1][i]);
        }
        printf("\n");
}
	return 0;
}
