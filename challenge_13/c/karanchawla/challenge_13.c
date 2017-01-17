//Karan Chawla
//Challenge 13

#include <stdio.h>
#include <stdlib.h>

// Dynamic Array Definition
//////////////////////////////////////////////////////////////////////////////////
typedef struct {
    int *array;
    size_t used;
    size_t size;
} Array;

void initArray(Array *a, size_t initialSize) 
{
    a->array = (int *)malloc(initialSize * sizeof(int));
    a->used = 0;
    a->size = initialSize;
}

void insertArray(Array *a, int element) 
{
// a->used is the number of used entries, because a->array[a->used++] updates a->used only *after* the array has been accessed.
// Therefore a->used can go up to a->size 
    if (a->used == a->size) 
    {
        a->size *= 2;
        a->array = (int *)realloc(a->array, a->size * sizeof(int));
    }
    a->array[a->used++] = element;
}

void freeArray(Array *a) 
{
    free(a->array);
    a->array = NULL;
    a->used = a->size = 0;
}
/*
Array a;
int i;
initArray(&a, 5);  // initially 5 elements
for (i = 0; i < 100; i++)
insertArray(&a, i);  // automatically resizes as necessary
printf("%d\n", a.array[9]);  // print 10th element
printf("%d\n", a.used);  // print number of elements
freeArray(&a);
*/
///////////////////////////////////////////////////////////////////////////////////

void isPalindrome(int num)
{
    Array a;
    initArray(&a,1);
    while(num)
    {
        insertArray(&a, num%10);
        num /= 10;
    }

    int size = a.used;

    int flag = 1;
    for(int i=0;i<size/2;i++)
    {
        if(a.array[i]==a.array[size-i-1])
        {
            flag = 1;
        }
        else 
        {
            flag = 0;
            break;
        }
    }

    if(flag) printf("True\n");
    else printf("False\n");

    freeArray(&a);
}


//Driver Program
int main(void)
{
    int num = 1234554321;

    isPalindrome(num);

    return 0;
}