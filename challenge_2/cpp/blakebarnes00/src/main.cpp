#include <iostream>
#include <algorithm>  // std::sort(), std::remove()
#include <vector>


void print_array(std::vector<int> array)
{
  std::cout << "Array: ";
  for(int i = 0; i < array.size(); i++)
  {
    std::cout << array.at(i) << " ";
  }
  std::cout << std::endl;
}

int main()
{
  std::vector<int> num_array = {2, 3, 4, 2, 3, 5, 4, 6, 4, 6, 9, 10, 9, 8, 7, 8, 10, 7};
  
  // Sort ant then print the array.
  std::sort(num_array.begin(), num_array.end());
  print_array(num_array);
  
  int i = 0;
  while(i < num_array.size())
  {
    /*
     * This if statement will check if the number is equal to the next one, and
     * if so it will remove all the numbers of that value in the entire vector
     * array.
     */
    if(num_array.at(i) == num_array.at(i + 1))
    {
      num_array.erase(std::remove(num_array.begin(), num_array.end(), +num_array[i]), num_array.end());
      
      // Here we print out the array just to see its progress.
      print_array(num_array);
    }
    else if(num_array.at(i) != num_array.at(i + 1))
    {
      // This will tell us if a value is duped or not.
      std::cout << num_array.at(i) << " is not a dupe.\n";
      i++;
    }
  }

  //print_array(num_array);
  return 0;
}
