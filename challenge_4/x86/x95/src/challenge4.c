#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>

// Tree Element (Exactly 24 Bytes in size by using 64-Bit Integer)
struct node
{
	int64_t data;
	struct node* rightchild;
	struct node* leftchild;
};

//Pointer to tree
struct node* tree;

//Function Prototypes
void initTree();
void destroyTree();
void traverseTree();
extern void invertTree(struct node* entry); //<-- ASM Method for inverting the tree

//Main Method
int main()
{
	printf("Initialize Tree...\n\n");
	initTree();
	printf("Root Data: %" PRId64 "\n", tree->data);
	printf("Right Node: %p\n",tree->rightchild);
	printf("Left Node: %p\n\n",tree->leftchild);
	printf("Traverse Tree in PostOrder:\n");
	traverseTree(tree);
	printf("\n\nInverting Tree...\n\n");
	invertTree(tree);
	printf("Traverse Tree in PostOrder:\n");
	traverseTree(tree);
	printf("\n\nCleaning up...\n");
	destroyTree();
	return 0;
}

//Fill tree with test values
void initTree()
{
	tree = calloc(1,sizeof(struct node));
	tree->data = 4;
	tree->rightchild = calloc(1,sizeof(struct node));

	tree->rightchild->data = 7;
	tree->rightchild->rightchild = calloc(1,sizeof(struct node));
	tree->rightchild->rightchild->data = 9;
	tree->rightchild->rightchild->rightchild = NULL;
	tree->rightchild->rightchild->leftchild = NULL;

	tree->rightchild->leftchild = calloc(1,sizeof(struct node));
	tree->rightchild->leftchild->data = 6;
	tree->rightchild->leftchild->rightchild = NULL;
	tree->rightchild->leftchild->leftchild = NULL;

	tree->leftchild = calloc(1,sizeof(struct node));
	tree->leftchild->data = 2;
	tree->leftchild->rightchild = calloc(1,sizeof(struct node));
	tree->leftchild->rightchild->data = 3;
	tree->leftchild->rightchild->rightchild = NULL;
	tree->leftchild->rightchild->leftchild = NULL;

	tree->leftchild->leftchild = calloc(1,sizeof(struct node));
	tree->leftchild->leftchild->data = 1;
	tree->leftchild->leftchild->rightchild = NULL;
	tree->leftchild->leftchild->leftchild = NULL;

}

//Traverse Tree in PostOrder
void traverseTree(struct node* entry)
{
	if(entry->leftchild != NULL)
	{
		traverseTree(entry->leftchild);
	}
	if(entry->rightchild != NULL)
	{
		traverseTree(entry->rightchild);
	}
	printf("%" PRId64 ", ", entry->data);
}

//Free Memory
void destroyTree()
{
	free(tree->rightchild->rightchild);
	free(tree->rightchild->leftchild); 
	free(tree->rightchild);

	free(tree->leftchild->rightchild);
	free(tree->leftchild->leftchild);
	free(tree->leftchild);

	free(tree);
}