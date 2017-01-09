#include <stdio.h>
#include <stdlib.h>

// typedefs
    typedef int KEY;
    
// structures
typedef struct _NODE{
    KEY key;
    int count;
    struct _NODE* next;
}NODE;

// function declarations
int findSingleInt(int *ary, int n, int *result);
void getInput(int **ary, int *n);
NODE** getSetHead(void);
NODE* createNode(KEY n);
void searchCreateNode(KEY n);

int main(void){
// local declarations
    int *zArr;
    int result;
    int n;
    int success;

// statements
    getInput(&zArr, &n);
    success = findSingleInt(zArr, n, &result);

    // if result is less than 0 no single integer was found
    if(success==1)
        printf("Single integer is: %d\n", result);
    else if(success > 1)
        printf("More than one single integer was found\n");
    else printf("No single integer found\n");

    return 0;
} // main
void getInput(int **ary, int *n){
// local declarations
    int i;

// statements
    printf("Please enter the size of the array: ");
    while(1){ // takes input till n > 0
        scanf("%d", n);
        
        if(*n > 0) break;
        printf("Please input a number larger than 0\n");
    } // while

    // allocate memory for the array
    *ary = malloc(sizeof(int) * (*n));

    // fill the array
    printf("Please fill in the integers for the array and\n");
    printf("remember that there should be one integer that does not repeat.\n");
    for(i = 0; i < *n; i++){
        scanf("%d", &(*ary)[i]);
    } // for
    
} // getInput
int findSingleInt(int *ary, int n, int *result){
// local declarations
    NODE **head;
    NODE *walker;
    int i;
    int success = 0;
    
// statements
    for(i = 0; i < n; i++)
        searchCreateNode(ary[i]); // creating all the nodes needed to find the single int

    head = getSetHead();
    for(walker = (*head)->next; walker; walker = walker->next){
        // if more than one single int, increment success to indicate failure
        if(walker->count == 1){ // if single int is found
            *result = walker->key;
            success += 1;
        } // if
    } // for

    return success;
} // findSingleInt

NODE** getSetHead(void){
// local declarations
    static NODE *head = NULL;

// Statements
    if(!head){ // if head is NULL, creates head
        if(!(head = malloc(sizeof(NODE)))){
            printf("Error when allocating memory\n");
            exit(-1);
        } // malloc went wrong
        head->next = NULL;
    }

    return &head;
} // getSetHead

NODE* createNode(int n){
// local declarations
    NODE *new;

    if(!(new = malloc(sizeof(NODE)))){
        printf("Error when allocating memory\n");
        exit(-1);
    }
    new->key = n;
    new->count++;
    new->next = NULL;

    return new;
} // createNode

void searchCreateNode(KEY n){
// local declarations
    NODE **head;
    NODE *new;
    NODE *walker;

// statements
    head = getSetHead();

    // if element is not pointing at an element create one
    if(!((*head)->next)){
        new = createNode(n);
        (*head)->next = new;
    }
    else{
        for(walker = (*head)->next; walker; walker = walker->next){
            if(walker->key == n){ // if finding the node, increment it's count
                walker->count++;
                break;
            }
            else if(walker->next == NULL){ // else create the node
                new = createNode(n);
                walker->next = new;
                break;
            }
        } // for
    } // else
} // searchCreateNode
