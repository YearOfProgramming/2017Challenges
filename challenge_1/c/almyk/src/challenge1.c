#include <stdio.h>
#include <string.h>

int main(void){
    char chArr[100];
    char temp;
    int n;

    printf("Enter string you want to see reversed: ");
    scanf("%99[^\n]", chArr);

    n = strlen(chArr);
    for(int i=0; i< n/2; i++){
        temp = chArr[i];
        chArr[i] = chArr[n - i - 1];
        chArr[n - i - 1] = temp;
    }
    printf("Reversed String: %s\n", chArr);

    return 0;
}
