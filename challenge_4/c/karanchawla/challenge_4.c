#include <stdio.h>
#include <stdlib.h> 

typedef struct node
{
	/* data */
	int data;
	struct node* left, *right;
}Node;

Node* newNode(int data)
{
	Node* newNode = (Node*) malloc(sizeof(Node));
	newNode->left = NULL;
	newNode->right = NULL;
	newNode->data = data;

	return newNode;
}

void invertTree(Node* head)
{
	if(head==NULL)
	{
		return;
	}
	else
	{
		Node* temp = head;
		invertTree(head->left);
		invertTree(head->right);

		temp = head->left;
		head->left = head->right;
		head->right = temp;
	}

	return;
}

void inOrder(struct node* node) 
{
  if (node == NULL) 
    return;

  inOrder(node->left);
  printf("%d ", node->data);
  inOrder(node->right);
}  

//Driver function
int main(void)
{
	struct node *root = newNode(4);
	root->left        = newNode(2);
	root->right       = newNode(7);
	root->left->left  = newNode(6);
	root->left->right = newNode(9); 
	root->right->left  = newNode(1);
	root->right->right = newNode(3);

	inOrder(root);
	
	printf("\n");

	invertTree(root);

	inOrder(root);
	return 0;
}