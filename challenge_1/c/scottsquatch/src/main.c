#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

/* Constants */
#define RETURN_SUCCESS 0
#define MAX_SIZE 256

/* Function Declarations */
char* reverse(char* originalString);
bool shouldContinue(char contineChar);

int main()
{
  char stringToReverse[MAX_SIZE];
  char continueResult;
  char* reversedString = NULL;

  do
  {
    // Get String to Reverse
    printf("Please Enter a string to reverse (%i characters max): ", MAX_SIZE);
    scanf("%s", stringToReverse);

    // Print result
    reversedString = reverse(stringToReverse);
    printf("Reversed String: %s\n", reversedString);

    // See if we should continue
    printf("Would you like to continue (y to continue): ");
    scanf(" %c", &continueResult);

  } while(shouldContinue(continueResult));

  // free up memory
  free(reversedString);

  return RETURN_SUCCESS;
}

// Reverse a given string.
char* reverse(char* originalString)
{
  // Variables
  int length;
  char* reversedString = NULL;
  int i;
  int reversedIndex;

  if (originalString != NULL)
  {
    length = strlen(originalString);
    reversedString = calloc(length, sizeof(char));
    reversedIndex = 0;

    // Iterate over Original String in Reverse
    for (i = length - 1; i >= 0; i--)
    {
      reversedString[reversedIndex++] = originalString[i];
    }
  }

  return reversedString;
}

// Return true if we are to continue loop
bool shouldContinue(char contineChar)
{
  return contineChar == 'y' || contineChar == 'Y';
}
