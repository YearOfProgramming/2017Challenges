#include <iostream>
#include <vector>
#include <algorithm>

void print_array(std::vector<int> array)
{
  for(int i = 0; i < array.size(); i++)
  {
    std::cout << array.at(i) << " ";
  }
  std::cout << std::endl;
}

int main()
{
  /*
   * Sort the given array from least to greatest. (This will make it easier to
   * sort out what is the greatest.
   */
  std::vector<int> array = {2, 2, 3, 7, 5, 7, 7, 7, 4, 7, 2, 7, 4, 5, 6, 7, 7,
    8, 6, 7, 7, 8, 10, 12, 29, 30, 19, 10, 7, 7, 7, 7, 7, 7, 7, 7, 7};
  std::sort(array.begin(), array.end());
  print_array(array);
  
  /*
   * Get the last number in the array (will be the max because we sorted
   * smallest to largest)
   */
  int max = array.back();

  /*
   * The idea behind using the counter like this is so that we can use it in
   * more than one place. 
   *
   * We allocate (in this case) 30 spaces + 1 buffer to prevent overflow.
   */
  int* counter = new int[max + 1]();

  for(int i = 0; i < array.size(); i++)
  {
    counter[array[i]]++;
  }

  int majority = 0;
  while(counter[majority] <= array.size()/2)
  {
    majority++;
  }

  std::cout << "Majority: " << majority << std::endl;
  delete[] counter; // Deollocate the memory

  return 0;
}
