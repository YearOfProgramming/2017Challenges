#include <iostream>
#include <string>

using namespace std;

string ReverseString(string input) {
  string output;
  for(int i = input.length() - 1; i >= 0; --i) {
	  output.push_back(input[i]);
  }

  return output;
}

int main(int argc, char** argv) {
  string input;
  string output;

  cout << "Please enter a string you wish to reverse: ";
  getline(cin, input);
  output = ReverseString(input);
  cout << "The reversed string is: " << output << endl;
  return 0;
}
