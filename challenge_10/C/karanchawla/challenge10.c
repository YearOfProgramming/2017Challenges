/*
karanchawla
Challenge #10
Check for balanced paranthesis
Using stack to check if the matching pair exists or not
*/

#include <stdio.h>
#include <stdlib.h> 
#include <limits.h> 
#include <string.h> 

#ifndef OK
#define OK 0
#endif

#ifndef NO_INPUT
#define NO_INPUT 1
#endif

#ifndef TOO_LONG
#define TOO_LONG 2
#endif


//structure for linked list node
typedef struct node
{
	int data;
	struct node* next;
}Node;

//utility function to create a new node
Node* newNode(int x)
{
	Node* stackNode = (Node*) malloc(sizeof(Node));
	stackNode->data = x;
	stackNode->next = NULL;
	return stackNode;
}

//utility function to check if linked list is empty
int isEmpty(Node* head)
{
	if(head->next==NULL)
		return 1;
	return 0;
}

//utility function to push a node to linked list
void push(Node** root, int x)
{
	struct node* stackNode = newNode(x);
	stackNode->next = *root;
	*root = stackNode;
	//use for debugging
	//printf("Pushed %d to the stack\n",x);
}

//utility function pop a node from the stack
char pop(Node** root)
{
	if(isEmpty(*root))
		return INT_MIN;

	Node* temp = *root;
	*root = (*root)->next;
	char popped = temp->data;

	free(temp);
	return popped;
}

//bool function to check if it's a matching pair or not
int isMatchingPair(char c1, char c2)
{
	if(c1== '(' && c2 == ')')
		return 1;
	else if(c1 == '[' && c2 ==']')
		return 1;
	else if(c1 == '{' && c2 =='}')
		return 1;
	else if(c1 == '<' && c2 =='>')
	else 
		return 0;
}

//function that checks for balanced paranthesis
int checkParathesisBalanced(char *str)
{
	int size = strlen(str);
	Node* stack = NULL;
	int i=0;

	while (str[i])
	{
		if(str[i]=='[' || str[i]=='(' || str[i]=='{' || str[i]=='<')
		{
			push(&stack,(int)str[i]);
		}

		if(str[i]=='}' || str[i]==')' || str[i]==']' || str[i]=='>')
		{
			if (stack==NULL)
				return 0;

			else if (!isMatchingPair(2pop(&stack),str[i]))
				return 0;
		}
		i++;
	}	

	if (stack==NULL)
		return 1;
	else
		return 0;
}

//utility function to safely get string input from user
static int getLine (char *prmpt, char *buff, size_t sz) {
    int ch, extra;

    // Get line with buffer overrun protection.
    if (prmpt != NULL) {
        printf ("%s", prmpt);
        fflush (stdout);
    }
    if (fgets (buff, sz, stdin) == NULL)
        return NO_INPUT;

    // If it was too long, there'll be no newline. In that case, we flush
    // to end of line so that excess doesn't affect the next call.
    if (buff[strlen(buff)-1] != '\n') {
        extra = 0;
        while (((ch = getchar()) != '\n') && (ch != EOF))
            extra = 1;
        return (extra == 1) ? TOO_LONG : OK;
    }

    // Otherwise remove newline and give string back to caller.
    buff[strlen(buff)-1] = '\0';
    return OK;
}

//Drive program. Takes a string 'buff' 
//from the user and checks for balanced paranthesis
int main(void)
{
	int out;
    char buff[10000];

    out = getLine ("Enter string> ", buff, sizeof(buff));
    if (out == NO_INPUT) {
        // Extra NL since my system doesn't output that on EOF.
        printf ("\nNo input\n");
        return 1;
    }

    if (out == TOO_LONG) {
        printf ("Input too long [%s]\n", buff);
        return 1;
    }

    printf ("OK [%s]\n", buff);

    if (checkParathesisBalanced(buff))
	    printf("\n True");
  	else
    	printf("\n False ");  
  
  return 0;
}