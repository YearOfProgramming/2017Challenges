#include <stdio.h>
#include <string.h>

int main(void){
    char chArr[100];
    int n;

    printf("Enter string you want to see reversed: ");
    scanf("%99[^\n]", chArr);

    n = strlen(chArr);
    for(int i=n-1; i>=0; i--) printf("%c", chArr[i]);
    printf("\n");

    return 0;
}
