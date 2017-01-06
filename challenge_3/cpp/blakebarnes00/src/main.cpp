#include <iostream>
#include <vector>
#include <algorithm>

<<<<<<< HEAD
/*
 * Here we call for a reference to the array (This prevents the compiler from
 * having to recreate the same variables over again for this function.
 */
void print_array(std::vector<int> &array)
{
  for(auto i : array)
  {
    std::cout << i << " ";
=======
void print_array(std::vector<int> array)
{
  for(int i = 0; i < array.size(); i++)
  {
    std::cout << array.at(i) << " ";
>>>>>>> 2656416c1f7b18d96165977753f57dc1a69928be
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
<<<<<<< HEAD
   * The counter has the max number in it, plus one so that it has a buffer
   * space so we won't overflow.
   */
  std::vector<int> counter(max + 1);

  for(auto i : array)
  {
    counter[i]++;
  }

  int majority = -1;
  for(int i = 0; i < counter.size(); i++)
  {
    if(counter[i] > array.size() / 2)
    {
      majority = i;
      break;
    }
  }
  if(majority < 0)
  {
    std::cerr << "Unable to find majority number.\n";
    return 0;
  }
  std::cout << "Majority: " << majority << std::endl;
=======
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
>>>>>>> 2656416c1f7b18d96165977753f57dc1a69928be

  return 0;
}
