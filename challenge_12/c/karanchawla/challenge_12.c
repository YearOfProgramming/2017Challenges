/*
Karan Chawla
Challenge 12
*/

#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 

#ifndef MAX
#define MAX 256
#endif


//function that counts the ocurrence of each element in the string
void zip(const char *a, size_t size)
{
	int count[MAX] = { 0 };
	int flag[MAX];

	for(int i=0;i<size;i++)
	{
		count[(int)(a[i])]++;
		flag[(int)(a[i])] = 1;
	}
	
	//for(int i=0; i<MAX; i++) printf("%d ", flag[i]);
	//if there's multiple occurences of chars
	for(int i=0 ; i<size; i++)
	{
		if(count[(int)a[i]]>1 && flag[(int)a[i]]==1)
		{
			printf("%c#%d",a[i],count[(int)a[i]]);
			flag[a[i]]=0;
		}
		else if(count[(int)a[i]]==1)
			printf("%c",a[i]);
	}

	return;
}

//driver program
int main(void)
{
	//example 1
	const char *str = "The quick brown fox jumped over the lazy dog.";
	size_t size = strlen(str);

	//function call to zip
	zip(str,size);

	return 0;
}