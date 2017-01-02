#include<stdio.h>
#include<string.h>
void main()
{
    char array[255],i;
    int flag,len,j;
    printf("Enter array of numbers: ");
    gets(array);
    for(len=0;array[len]!='\0';len++);
    len-=1;

    //Run every number from 0 to 9 and if matching, flag+=1
    //This has a runtime of O(11n) I think. That's linear right ?
    
    for(i='0';i<='9';i++){
	flag=0;
	for(j=0;j<=len;j++)
	    if (array[j]==i)
		flag++;
	if(flag==1)
	    printf("%c",i);
    }
}
