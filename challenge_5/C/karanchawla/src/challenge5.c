/*
Author: Karan Chawla
Challenege #5
Expected Running time O(k + n log n)
where k is the position of the char in the new sorted string
*/

#include <stdio.h>
#include <stdlib.h> 
#include <time.h> 
#include <string.h>


//utility function used by qsort to sort the strings
int comp (const void * elem1, const void * elem2) 
{
    char f = *((char*)elem1);
    char s = *((char*)elem2);
    if (f > s) return  1;
    if (f < s) return -1;
    return 0;
}

//function to shuffle the string
void shuffle(char *array, size_t n)
{
    if (n > 1) 
    {
        size_t i;
        for (i = 0; i < n - 1; i++) 
        {
            size_t j = i + rand() / (RAND_MAX / (n - i) + 1);
            char t = array[j];
            array[j] = array[i];
            array[i] = t;
        }
    }
}

//utility function to print array
void printArray(char *a, int size)
{
    for(int i=0;i<size;i++) printf("%c", a[i]);
}

int main(void)
{   
    srand(time(NULL));

    //First string cannot be empty
    char s[] = "alkugfv";
    int size = sizeof(s)/sizeof(*s);
    char t[size + 1];
    strcpy(t,s);
    
    //edge case
    if(size==0)
        continue;
    else
        shuffle(s,size-1);
    
    //Insert the char e at a random position
    int pos = rand() % (size-1);
    
    for(int i=0;i<size;i++)
    {
        char temp;

        if(i==pos)
        {
            temp = t[i];
            t[i] = 'd';
        }

        t[size-1] = temp;
    }

    
    //Sort the two strings
    qsort(s,size-1,sizeof(*s),comp);
    qsort(t,size,sizeof(*t),comp);
    
    char extraChar[1];
    int flag = 0;

    //find the added character
    for(int i=0; i<size-1; i++)
    {
        if(t[i]!=s[i])
        {
            extraChar[0] = t[i];
            flag = 1;
            break;
        }
        else
            continue;

    }

    //print the answer
    if(flag==0)
    {
        printf("%c\n",t[size-1]);
    }
    else
        printf("%c\n", extraChar[0]);

    return 0;
}