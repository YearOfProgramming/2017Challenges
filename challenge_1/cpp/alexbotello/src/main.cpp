#include <iostream>
#include <string>
using namespace std;

int main()
{
  string input;

  cout << ">: ";
  getline(cin, input);

  for (int i = input.length(); i >= 0; i--)
  {
    cout << input[i];
  }
  cout << endl;

  return 0;
}
