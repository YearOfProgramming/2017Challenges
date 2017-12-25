#include <stdlib.h>
#include <stdio.h>

/** Constants **/
#define MODE_READ  "r"
#define NUM_ARGS 3
#define FILE_NAME_ARG 1
#define ARRAY_SIZE_ARG 2

/** Function Prototypes **/
int int_compare(const void*, const void*);
void print_array(int*, int);
int get_majoriy_element(int*, int);
int* read_array(char*,int);

int main(int argc, char* argv[])
{
  // Get parameters from input
  if (argc != NUM_ARGS)
  {
    // Incorrect number of parameters
    printf("Incorrect Number of parameters, expected %d but got %d\n",
      NUM_ARGS - 1, argc - 1);
    printf("Usage: ./majority_element <array file> <size of array in file>\n");
  }
  else
  {
    // Read array from file
    char* fileName = argv[FILE_NAME_ARG];
    int arraySize = atoi(argv[ARRAY_SIZE_ARG]);
    int* input_array = read_array(fileName, arraySize);

    // Output to Screen for informational purpose
    printf("array: ");
    print_array(input_array, arraySize);
    printf("\n");

    // Print Majority Element
    printf("Majority Element: %d\n", get_majoriy_element(input_array, arraySize));

    // Free memory
    free(input_array);
  }
}

// Read array from FILE
int* read_array(char* fileName, int arraySize)
{
  int* array = calloc(arraySize, sizeof(int));
  FILE *input = fopen(fileName, MODE_READ);
  int index = 0;

  // Read data directly into array.
  while (fscanf(input, "%*c %d", &array[index++]) == 1
    && (index < arraySize))
  { }

  // close input FILE
  fclose(input);

  return array;
}

// Obtain the majority element of the array
int get_majoriy_element(int* array, int size)
{
  qsort(array, size, sizeof(int), int_compare);

  // For debugging purposes
  printf("sorted array: ");
  print_array(array, size);
  printf("\n");

  // After sorting array the n/2 element will always be the majority element
  return array[size/2];
}

// Compare two integers.
// - Return negative num if first < second
// - Return 0 if first == second
// - Return positive num if first > second
int int_compare(const void* first, const void* second)
{
  return (*(int*)first) - (*(int*)second);
}

// Print array to console
void print_array(int* array, int size)
{
  for (int i = 0; i < size; i++)
  {
    printf("%d ", array[i]);
  }
}
