//Karan Chawla
//Challenge 11

#include <stdio.h>
#include <stdlib.h> 

typedef struct node
{
	int data;
	struct node* left, *right;
}Node;

Node* newNode(int data)
{
	Node* node = (Node*)malloc(sizeof(Node));

	node->data = data;
	node->left = NULL;
	node->right = NULL;

	return node;
}

Node* insert(Node* node, int data)
{
	if(node==NULL) return newNode(data);

	if(data>node->data)
	{
		node->right = insert(node->right,data);
	}
	else 
	{
		node->left = insert(node->left,data);
	}
	return node;
}

void preOrder(Node* node)
{
	if(node==NULL)
		return;

	printf("%d\n",node->data);

	preOrder(node->left);
	preOrder(node->right);

	return;
}

Node* findSmallest(Node* node)
{
	while(node->left!=NULL)
	{
		node = node->left;
	}

	return node;
}

Node* findLargest(Node* node)
{
	while(node->right!=NULL)
	{
		node = node->right;
	}

	return node;
}

/*
3 caes for node deletion from BST:
1. Node to be deleted is leaf.
2. Node to be deleted has one child. 
3. Node to be deleted has two children.
*/
Node* deleteNode(Node* node, int key)
{
	//base case
	if(node==NULL)
		return node;

	//search in right subtree
	if(key>node->data)
	{
		deleteNode(node->right,key);

	}
	//search in left sub tree
	else if(key<node->data)
	{
		deleteNode(node->left,key);
	}
	//if key is equal to node->data
	else 
	{
		//has only right child - copy the child to the node
		//and delete node
		if(node->left==NULL)
		{
			Node* tempNode = node->right;
			free(node);
			return tempNode;
		}
		if(node->right==NULL)
		{
			Node* tempNode = node->left;
			free(node);
			return tempNode;
		}
		//has two children
		//find the successor using findsmallest in right subtree
		//copy it to the node and delete the successor node. 
		else
		{
			Node* tempNode = findSmallest(node->right);
			node->data = tempNode->data;
			node->right = deleteNode(node->right,tempNode->data);
		}
	}

	return node;
}

//driver function
int main(void)
{
	//Example 1
	/*
	struct node *root = NULL;
    root = insert(root, 1);
    root = insert(root, 2);
    root = insert(root, 3);
    root = insert(root, 4);
    root = insert(root, 7);
    root = insert(root, 6);
    root = insert(root, 8);
    */

    //number of nodes input
    printf("Enter the numer of nodes you want in the BST:\n");
    int t;
    scanf("%d",&t);

    //node data input
    printf("Now enter the node data values\n");

    //Tree initialization
    Node* root = NULL;

    //data values from user 
    while(t--)
    {
    	int key;
    	scanf("%d",&key)
    	root = insert(root,key);
    }

    printf("Before deletion your BST looks like:\n");

    preOrder(root);
    deleteNode(root,70);

    printf("After deletino the BST looks like\n");
    preOrder(root);

    return 0;
}