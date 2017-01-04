#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node{
    int value;
    struct node *left;
    struct node *right;
} Node;

void tr_add(Node *pos, int val);
Node *nd_malloc(int val);
void disp_tree(char *message);
void disp_node(Node *pos, int depth, int dire);
void invert_tree(Node *pos);

Node *root = NULL;

int main(void)
{
    // Add all nodes to the root
    tr_add(root, 4);
    tr_add(root, 2);
    tr_add(root, 7);
    tr_add(root, 1);
    tr_add(root, 3);
    tr_add(root, 6);
    tr_add(root, 9);

    disp_tree("Before\n");

    invert_tree(root);
    disp_tree("After\n");
    
    return 0;
}

void tr_add(Node *pos, int val)
{
    Node *dt = nd_malloc(val);

    // For the root
    if(pos == NULL) root = dt;
    else if(val > pos->value){
        if(pos->right == NULL) pos->right = dt;
        else tr_add(pos->right, val);
    }
    else if(val < pos->value){
        if(pos->left == NULL) pos->left = dt;
        else tr_add(pos->left, val);
    }
    else return;
}

Node *nd_malloc(int val)
{
    // Allocate memory for a node
    Node *nd;

    if((nd = (Node *)malloc(sizeof(Node))) == NULL){
        printf("Uable to allocate memory\n");
    }
    nd->value = val;
    nd->left = NULL;
    nd->right = NULL;

    return nd;
}

void disp_tree(char *message)
{
    printf("%s", message);

    // Display all nodes in a console
    disp_node(root, 0, 'T');
}

void disp_node(Node *pos, int depth, int dire)
{
    if(pos == NULL) return;
    disp_node(pos->right, depth+1, 'R');
    if(dire == 'R') printf("%*s%s", depth*6, "", "/---");
    if(dire == 'T') printf("    ");
    if(dire == 'L') printf("%*s%s", depth*6, "", "\\---");
    printf("%d\n", pos->value);
    disp_node(pos->left, depth+1, 'L');
}

void invert_tree(Node *pos)
{
    // Traverse each node in post-order
    if(pos->left != NULL) invert_tree(pos->left);
    if(pos->right != NULL) invert_tree(pos->right);

    // Swap left and right node by its pointer
    Node *tmp = pos->left;
    pos->left = pos->right;
    pos->right = tmp;
}
