#include <iostream> 

// I tried to solve this challenge using only the <iostream> library

using namespace std;

int main(int argc, char* argv[])
{
 	// First we check inputs from the command line
	// if there are no strings from the command line
	// we wait for a string as input.
	// The control (if) is don on the variable argv[1]
	// argv[0] is reserved to the name of the program

	// In both cases the output is generated using a for loop.
	// The starting point for reading the string, i.e. its end,
	// is obtained with the function strlen()

	if (argv[1]!=NULL)
	{
		for (int i = argc - 1; i > 0; --i)
		{
			for (int j=strlen(argv[i]);j>=0;j--)
			{
			 cout << argv[i][j];
			}
	 	cout <<endl;
		}
	}else
	{
 
		char *x;
		cout<< "Please insert a String!!!!!! >> ";
		cin>>x;
		
		for (int j=strlen(x);j>=0;j--)
		{
			cout << x[j]; 
		}
		cout<<endl;
	}
	return 0;
}