#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 128

int findSingleInt(int *ary, int n);
void getInput(int **ary, int *n);

int main(void){
    // local declarations
    int *zArr;
    int result;
    int n;

// statements
    getInput(&zArr, &n);
    result = findSingleInt(zArr, n);

    // if result is less than 0 no single integer was found
    if(result>=0)
        printf("Single integer is: %d\n", result);
    else printf("No single integer found\n");

    return 0;
} // main
void getInput(int **ary, int *n){
// local declarations
    int i;

// statements
    printf("Please enter the size of the array: ");
    scanf("%d", n);

    // allocate memory for the array
    *ary = malloc(sizeof(int)**n);

    // fill the array
    printf("Please fill in the integers for the array and\n");
    printf("remember that there should be one integer that does not repeat.\n");
    for(i = 0; i < *n; i++){
        scanf("%d", &(*ary)[i]);
    } // for
    
} // getInput
int findSingleInt(int *ary, int n){
// local declarations
    int *map;
    int max=0;
    int i;
    int result=-1;
    
// statements
    for(i = 0; i < n; i++)
        if(max < ary[i]) max = ary[i]; // find the largest value

    // allocate memory for array to keep track of integers
    map = malloc(sizeof(int)*max+1); 
    for(i = 0; i < n; i++){
        if(ary[i] < 0) continue; // don't accept negative values
        map[ary[i]]++;
    } // for
    for(i = 0; i <= max; i++)
        if(map[i] == 1) result = i; // finding the single integer

    return result;
} // findSingleInt
