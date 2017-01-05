#include <iostream>
#include <string>
#include <algorithm>

int main()
{
  std::string input_string="";

  /*
   * We have to use getline() because std::cin by itself will not return the
   * entire line we input.
   */
  std::cout << "Please enter string: ";
  getline(std::cin, input_string);

  // Show the user the input before it is reversed
  std::cout << "\"" << input_string << "\"" << " when reversed is: ";
  
  /*
   * It is not needed to assign the string to a new variable, but I did it just
   * to make the code more readable
   *
   * First we initialize and then reassign the string to a new one, then revese
   * the new string.
   */
  std::string reversed_string = input_string; 
  reverse(reversed_string.begin(), reversed_string.end());

  std::cout << reversed_string << std::endl;

  return 0;
}
