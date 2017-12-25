#include <stdio.h>
#include <string.h>
#include <stdlib.h>
struct bst {
    int x;
    int occ;
    struct bst *left;
    struct bst *right;
};
void freeBST(struct bst *head) {
    if (head==NULL) return;
    if (head->left!=NULL) freeBST(head->left);
    if (head->right!=NULL) freeBST(head->right);
    free(head);
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
int majorityElement(int *nums, int length) {
    if (!nums) return -1;
    int element = nums[0];
    struct bst *head = malloc(sizeof(struct bst));
    head->x=nums[0];
    head->occ =1;
    head->left = NULL;
    head->right = NULL;
    for (int i=1; i<length; i++) {
        int occ = addNum(nums[i],head);
        if (occ>(length/2)) element=nums[i];
    }
    if (head) freeBST(head);
    return element;
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

    printf("%d\n", majorityElement(nums, length));

    if (input) free(input);
    if (nums) free(nums);
    return 0;
}
