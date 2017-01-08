#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* Constants */
#define RETURN_SUCCESS 0
#define MAX_SIZE 256
#define TRUE 0
#define FALSE -1

/* Function Declarations */
void reverse(char* originalString);
int should_continue(char contineChar);
void swap(char*, int, int);

int main()
{
  char stringToReverse[MAX_SIZE];
  char continueResult;

  do
  {
    // Get String to Reverse
    printf("Please Enter a string to reverse (%i characters max): ", MAX_SIZE);
    scanf("%s", stringToReverse);

    // Print result
    reverse(stringToReverse);
    printf("Reversed String: %s\n", stringToReverse);

    // See if we should continue
    printf("Would you like to continue (y to continue): ");
    scanf(" %c", &continueResult);

  } while(should_continue(continueResult) == TRUE);

  return RETURN_SUCCESS;
}

// Reverse a given string.
void reverse(char* originalString)
{
  if (originalString != NULL)
  {
    int length = strlen(originalString);
    int backIdx = length - 1;
    // Calculate number of loops here so that we don't have to keep recomputing.
    // swapping front and back pointers so only iterate over half of length
    int numLoops = length / 2;

    // iterate over half of the string, swapping front and back pointers
    for (int frontIdx = 0; frontIdx < numLoops; frontIdx++)
    {
      // Swap back and front to reverse string.
      swap(originalString, frontIdx, backIdx--);
    }
  }
}

// Swap characters of a character array
void swap(char* string, int firstIndex, int secondIndex)
{
  char temp = string[firstIndex];
  string[firstIndex] = string[secondIndex];
  string[secondIndex] = temp;
}

// Return true if we are to continue loop
int should_continue(char contineChar)
{
  if (contineChar == 'y' || contineChar == 'Y')
  {
    return TRUE;
  }
  else
  {
    return FALSE;
  }
}
