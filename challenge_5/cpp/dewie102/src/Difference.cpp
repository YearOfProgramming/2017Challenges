#include <iostream>
#include <string>
#include <cstdlib>
#include <time.h>

using namespace std;

char FindDifference (string l_a, string l_b) {
	if (l_a.size () != l_b.size ()) {
		string smallest;
		string largest;
		if (l_a.size () > l_b.size ()) {
			smallest = l_b;
			largest = l_a;
		} else {
			smallest = l_a;
			largest = l_b;
		}

		while (smallest.size () != 0) {
			for (int i = 0; i < largest.size (); i++) {
				if (smallest[smallest.size () - 1] == largest[i]) {
					smallest.pop_back ();
					largest.erase (largest.begin() + i);
					continue;
				}
			}
		}

		return largest[0];
	}
	
	return ' ';
}

string RandomString (string l_input) {
	string result;
	result.resize (l_input.size ());
	int randNum;

	for (int i = 0; i < result.size (); i++) {
		randNum = rand() % l_input.size ();
		result[i] = l_input[randNum];
		l_input.erase (l_input.begin () + randNum);
	}

	randNum = rand () % 26 + 97;
	result.insert (result.begin () + (rand () % result.length()), (char)randNum);

	return result;
}

int main (int argc, char** argv) {
	srand (time (NULL));

	string s = "abcd";
	string t = "abcde";

	string randomString = RandomString (s);

	char difference = FindDifference (s, t);
	cout << "Originial String: " << s << "\nRandom String: " << t << endl;
	cout << "The difference between the strings is: " << difference << endl;

	return 0;
}