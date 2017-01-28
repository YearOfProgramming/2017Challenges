#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int main()
{
	// user input
	string s, sSorted;
	cout << "Please enter the string s: "; //ask for input
	cin >> s;
	sSorted=s;

	string t, tSorted;
	cout << "Please enter the string t: "; //ask for input
	cin >> t;
	tSorted=t;


	// we use the copy of s and t (sSorted,tSorted) to have
	// the ordered list of char

     	sort(sSorted.begin(), sSorted.end());
	sort(tSorted.begin(), tSorted.end());
	

	// now that the two list are sorted we look for the first occurence where they differ
	bool not_found=1; 
	int i=0;
	while(i< sSorted.length() && not_found)
	{

		if(sSorted[i]!= tSorted[i]){
			cout<<"found diff: "<< tSorted[i]<<endl;
			not_found=0;
		} 
		i++;
	}

	// if while reading all the list until the length sSorted.length()
	// we haven’t found the char added to the original list, it means that it is in the last position of our
	// ordered list

	if (not_found)
	{
		cout<<"found: "<< tSorted[tSorted.length()-1]<<endl;
	}
return(0);

}