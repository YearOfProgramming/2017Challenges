#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> input = { 2, 2, 3, 7, 5, 7, 7, 7, 4, 7, 2, 7, 4, 5, 6, 7, 7, 8, 6, 7, 7, 8, 10, 12, 29, 30, 19, 10, 7, 7, 7, 7, 7, 7, 7, 7, 7 };
unordered_map<int, int> map;

void CountElements (vector<int> l_elements) {
	for (int i = 0; i < l_elements.size (); i++) { // Iterate through all elements in the vector
		auto it = map.find (l_elements[i]); // Obtain the iterator pointing to the element in the map at the ith position of the input vector
		if (it != map.end ()) {
			it->second++; // If the element is present in the map, increase the count.
		} else {
			map.emplace (l_elements[i], 1); // Else create the element in the map and start its count at 1
		}
	}
}

int FindMajority () {
	for (const auto& it : map) { // Cycle through each element in the map
		if (it.second > (map.size () / 2)) { 
			return it.first; // If the count is greater than the input vector size / 2 then return the element with that count
		}
	}

	return INT_MIN; // Else return the smallest number possible for error checking, as it is unlikely this function will return this number normally
}

int main (int argc, char** argv) {
	CountElements (input); // Count the elements and create the map
	int result = FindMajority (); // Find and store the element that shows up the most
	
	// If the result is not equal to the smallest integer, then output the result. Else output there was an error
	string output = (result != INT_MIN ? to_string(result) : "Error: Majority Element not found");
	
	// Print out original input array and what the majority element was
	cout << "Given the array: [";
	for (int i = 0; i < input.size (); i++) {
		cout << input[i] << ",";
	}
	cout << "]\nThe Majority Element is: " << output << endl;

	return 0;
}
