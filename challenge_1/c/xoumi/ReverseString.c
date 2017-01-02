#include<stdio.h>
void main()
{
    int i,j;
    char *string,temp;
    printf("Enter string: ");
    gets(string);
    for(i=0;string[i]!='\0';i++);
    i-=1;
    for(j=0;j<i/2;j++){
	temp=string[j];
	string[j]=string[i-j];
	string[i-j]=temp;
    }
    printf("Reversed string is %s \n", string);
}
	

	



