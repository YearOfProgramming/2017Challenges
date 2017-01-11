/*
Author: karanchawla
Random Deep Copy
#Challenge #8
*/

#include <stdio.h> 
#include <stdlib.h> 


//node definition for the linked list
typedef struct node
{
	int data;
	struct node* next;
	struct node* random;
}Node;

//typedef struct node* Node;

//utility function to create a node
Node* newNode(int key)
{
	Node* temp = (struct node*) malloc(sizeof(struct node));

	temp->data = key;
	temp->next = NULL;
	temp->random = NULL;

	return temp;
}

//utility function to print the list
void printList(Node* head)
{
	while(head!=NULL)
	{
		if(head->random!=NULL)
		{
			printf("Node key: %d\t", head->data);
			printf("Random Node pointer data: %d\n", head->random->data);
		}
		else
		{
			printf("Node key: %d\t", head->data);
			printf("Random Node pointer data: NULL\n");
		}
		head = head->next;
	}
	return;
}

//First step is to insert a copy of each node
//after the first node in the original list
//Copy the random pointers
//Separate this second list
Node* deepCopy(Node* head)
{
	Node* old;
	Node* temp = head;
	//modify this list
	while(temp)
	{

		Node* temp2 = newNode(temp->data);
		old = temp->next;
		temp->next = temp2;
		temp2->next = old;
		temp = old;
	}

	temp = head;
	//copy arbitrary matching
	while(temp && temp->next)
	{
		if(temp->random==NULL)
		{
			temp->next->random = NULL;	
		}
		else
			temp->next->random = temp->random->next;
		
		temp = temp->next->next;
	}

	//Separating the two lists
	Node* newNode = head->next;
	temp = head; 

	while(temp)
	{
		old = temp->next;
		temp->next = old->next;
		temp = old->next;
		if(old->next) old->next->next;
	}

	return newNode;
}

//Driver program;
int main(void)
{
	Node* head = newNode(1);
	head->next = newNode(2);
	head->next->next = newNode(3);
	head->next->next->next = newNode(4);
	head->next->next->next->next = newNode(5);
	head->next->next->next->next->next = NULL;
	
	// Assign random Pointers
	head->random = head->next->next;
	head->next->random = head->next->next->next;
	head->next->next->random = NULL;
	head->next->next->next->random = head->next;
	head->next->next->next->next->random = head->next->next->next->next;

	printList(head);
	Node* deepCopyList = deepCopy(head);

	printList(deepCopyList);

	return 0;
}
