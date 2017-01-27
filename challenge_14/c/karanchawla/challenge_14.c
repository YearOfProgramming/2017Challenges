//Karan Chawla
//Challenge 14

#include <stdio.h>
#include <stdlib.h>

//Linked list node definition
typedef struct node
{
	char c;
	struct node* next;
}Node;


//utility function to create a new node
Node* newNode(char c)
{
	Node* new_node = (Node*)malloc(sizeof(Node));
	new_node->c = c;
	new_node->next = NULL;

	return new_node;
}

//utility function to add a new node to the linked list
void push(Node** head_ref, char c)
{
	Node* new_node = newNode(c);

	new_node->next = *head_ref;

	*head_ref = new_node;
}


//function to reverse the linked list
//prev->curr->next
//changes prev to next and moves current along the linked list until NULL
void reverseLinkedList(Node** head_ref)
{
	if (*head_ref==NULL)
		return;

	Node* prev = NULL;
	Node* current = *head_ref;
	Node* next;
	while(current!=NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head_ref = prev;
}

//utility function to print linked list
void printLinkedList(Node* head)
{
	while(head!=NULL)
	{
		printf("%c->", head->c);
		head = head->next;
	}
	printf("NULL\n");
}

//driver program
int main(void)
{
	Node* head = NULL;
	//create a linked list with chars from "murder"
	push(&head,'r');
	push(&head,'e');
	push(&head,'d');
	push(&head,'r');
	push(&head,'u');
	push(&head,'m');

	//print the linked list
	printLinkedList(head);
	//reverse the linked list
	reverseLinkedList(&head);
	//print the reversed linked list
	printLinkedList(head);

	return 0;
}
