#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//#define DBG 1
#if DBG
#define DBGPRINT printf
#else
#define DBGPRINT(...) /**/
#endif
char *readLine() {
    int length = 1;
    char *string = malloc(sizeof(char)*1);
    char *temp=NULL;
    char c;
    while (EOF!=(c=getchar()) && '\r'!=c && '\n' != c) {
        temp=realloc(string,length+1);
        if (temp==NULL) {
            printf("Error, unable to allocate any more memory for string\n");
            return NULL;
        }

        string=temp;
        string[length-1]=c;
        length++;
    }
    string[length]='\0';
    return string;
}

struct bst {
    int x;
    int occ;
    struct bst *left;
    struct bst *right;
};
struct list {
    int x;
    struct list *next;
};
void printList(struct list *head) {
    struct list *temp = head;
    printf("Printing list: ");
    while (temp!=NULL) {
        printf("%d ", temp->x);
        temp=temp->next;
    }
    printf("\nDone printing list\n");
}
void freeBST(struct bst *head) {
    if (head==NULL) return;
    if (head->left!=NULL) freeBST(head->left);
    if (head->right!=NULL) freeBST(head->right);
    free(head);
}
//given a number and the head of the bst,add it to the tree
//returns the number of occurences
struct list* addToList(struct list *head, int x) {
    struct list *cur;
    DBGPRINT("Add to list called with %d\n", x);
    if (head==NULL) {
        //  DBGPRINT("ADD TO LIST, HEAD IS NULL");
        cur=malloc(sizeof(struct list));
        cur->x=x;
        cur->next=NULL;
        return cur;
    }
    cur = head;

    //DBGPRINT("Add to list, head is NOT NULL");
    while (cur->next!=NULL) {
        cur=cur->next;
    }
    struct list *temp = malloc(sizeof(struct list));
    temp->x = x;
    temp->next = NULL;
    cur->next = temp;
    return head;
}
//return the new head of the list after deleting the item
struct list *delFromList(struct list *head, int x) {
    DBGPRINT("delfromlist called with %d\n", x);
    struct list *cur = head;
    if (cur==NULL) {
        DBGPRINT("Delfromlist called with a null head!");
        return NULL;
    }
    if (cur->x==x) {
        DBGPRINT("del from list found at head\n");
        cur=cur->next;
        free(head);
        return cur;
    }
    struct list *prev = NULL;
    while (cur!=NULL) {
        if (cur->x==x) {
            //if we've found our item we delete this entry
            if (prev==NULL) {//we're at the head of our list
                return cur->next;//return the next entry as the new head
            } else {
                struct list *temp = cur;
                prev->next=cur->next;
                free(temp);
                return head;
            }
        }
        else {
//update the pointers
            prev=cur;
            cur=cur->next;
        }
    }
    DBGPRINT("number not found, returning head");
    return head;//if we never found the number, just return the head
}
int addNum(int num, struct bst *head) {
    struct bst *cur = head;
    while (1) {
        if (num==cur->x) {
            cur->occ++;    //if the number is already in the tree increase it's occurence
            return cur->occ;
        }
        if (num<cur->x) {
            if (cur->left==NULL) {
                struct bst *new = malloc(sizeof(struct bst));
                new->x = num;
                new->occ = 1;
                new->left = NULL;
                new->right = NULL;
                cur->left = new;
                return new->occ;
            } else cur = cur->left;
        } else if (num>cur->x) {
            if (cur->right ==NULL) {
                struct bst *new = malloc(sizeof(struct bst));
                new->x = num;
                new->left = NULL;
                new->right = NULL;
                new->occ=1;
                cur->right = new;
                return new->occ;
            } else cur=cur->right;
        }
    }
}
//given a number and the head of the bst, return 1 if number is in tree or 0 otherwise
int numInTree(int num, struct bst *head) {
    struct bst *cur = head;
    while (1) {
        if (cur==NULL) return 0;
        if (num==cur->x) return 1;
        if (num<cur->x) cur=cur->left;
        else if(num>cur->x) cur = cur->right;
    }
}
//given an array of numbers of length, return the number that only occurs once
//
int singleNumber(int *numbers, int length) {
    int n=0;//n tracks the array in our possiblenumbers
    struct list *myList = NULL;
    myList=addToList(myList,numbers[0]);
    //printList(myList);
    struct list *temp = myList;

    DBGPRINT("adding %d to the list\n", numbers[0]);
    if (length==0) return -1;
    struct bst *head = malloc(sizeof(struct bst));
    head->x = numbers[0];//first number in the list will be the head and will be in our possible numbers array
    head->left = NULL;
    head->right = NULL;
    head->occ=1;
    for (int i=1; i<length; i++) {
        int occ = addNum(numbers[i],head);
        if (occ==1) {
            //first occ, add to list of possibilities
            myList=addToList(myList,numbers[i]);
            //printList(myList);
        } else {
            myList=delFromList(myList,numbers[i]);
        }

    }
    if (myList==NULL) {
        DBGPRINT("can't find a value\n");
        return -1;
    }
    if (myList->next!=NULL) {
        printf("mutliple potential values found!\n");
    }
    int number = myList->x;
    struct list *k = myList;
    struct list *prev = NULL;
    while (k!=NULL) {
        prev=k;
        k=k->next;
        free(prev);
    }
    freeBST(head);
    return number;
}
int main() {
    int *nums = malloc(sizeof(int));
    int length=0;
    char *input = readLine();
    if (input==NULL) {
        printf("unable to read input!\n");
        return -1;
    }
    char *ptr=NULL;
    ptr = strtok(input,",");
    while (ptr!=NULL) {
        int a = atoi(ptr);
        length++;
        if (length>1) nums=realloc(nums,(length+1)*sizeof(int));
        nums[length-1]=a;
        ptr=strtok(NULL, ",");
    }

    printf("%d\n", singleNumber(nums, length));
    free(input);
    free(nums);
}

