// Includes
#include <stdio.h>
#include <stdlib.h>

// Constants
#define MAP_SIZE 256

// Function Prototypes
int* get_frequency_map(char*, int);
char* get_input_array(int);
void output_single_characters(int*);

int main()
{
  int arraySize;
  char* inputArray;
  int* freqMap;

  printf("Please enter size of array ( 0 or less to quit): ");
  scanf("%d", &arraySize);

  while(arraySize > 0)
  {
    inputArray = get_input_array(arraySize);

    freqMap = get_frequency_map(inputArray, arraySize);

    output_single_characters(freqMap);

    // free memory
    free(freqMap);
    free(inputArray);

    printf("Please enter size of array ( 0 or less to quit): ");
    scanf("%d", &arraySize);
  }
}

// Print characters which appear only once in array
void output_single_characters(int* freqMap)
{
  printf("The following characters appear only once in the array:\n");
  for (int i = 0; i < MAP_SIZE; i++)
  {
    if (freqMap[i] == 1)
    {
      printf("%c ", (char)i);
    }
  }
  printf("\n");
}

// Obtain input from the user
char* get_input_array(int size)
{
  char* array = malloc(size * sizeof(char));

  for (int i = 0; i < size; i++)
  {
    printf("Please enter a character: ");
    scanf(" %c", &array[i]);
  }

  return array;
}

// Obtain a map of character to frequency. Index represents a char and
// value is the number of occurrences in the array
int* get_frequency_map(char* array, int size)
{
  int* frequencyMap = malloc(MAP_SIZE * sizeof(int));

  // Loop over array
  for (int i = 0; i < size; i++)
  {
    // Index is character number
    frequencyMap[(int)array[i]]++;
  }

  return frequencyMap;
}
