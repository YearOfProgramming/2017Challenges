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

  for(int i = 0; i < num_array.size(); i++)
  {
    if(num_array.at(i) == num_array.at(i + 1))
    {
      std::cout << num_array.at(i) << " is duped\n";
      num_array.erase(std::remove(num_array.begin(), num_array.end(), num_array.at(i)), num_array.end());
      print_array(num_array);
    }
    else
    {
      std::cout << num_array.at(i) << " is not duped.\n";
    }
  }


  print_array(num_array);
  return 0;
}
