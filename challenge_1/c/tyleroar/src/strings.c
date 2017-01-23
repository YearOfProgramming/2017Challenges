#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char *readLine() {
    int length = 1;
    char *string = NULL;
    char c;
    while (EOF!=(c=getchar()) && '\r'!=c && '\n' != c) {
        string=realloc(string,length);
        string[length-1]=c;
        length++;
    }
    string[length-1]='\0';
    return string;
}
int main(int argc, char **argv) {
    char *input = readLine();
    char temp;
    int length=0, i=0;
    for (temp=input[length]; temp!='\0'; length++) temp=input[length];
    length--;
    char *output = (char*) malloc(sizeof(char)*(length+1));
    if(length==0) {
        output[0]='\0';
    }
    else {
        for (i=0; i<length; i++) {
            output[i]=input[length-i-1];
        }
        output[i]='\0';
    }
    printf("%s\n", output);
}
