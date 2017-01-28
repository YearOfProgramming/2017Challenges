#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> input = { 2, 2, 3, 7, 5, 7, 7, 7, 4, 7, 2, 7, 4, 5, 6, 7, 7, 8, 6, 7, 7, 8, 10, 12, 29, 30, 19, 10, 7, 7, 7, 7, 7, 7, 7, 7, 7 };
unordered_map<int, int> map;

void CountElements (vector<int> l_elements) {
	for (int i = 0; i < l_elements.size (); i++) {
		auto it = map.find (l_elements[i]);
		if (it != map.end ()) {
			it->second++;
		} else {
			map.emplace (l_elements[i], 1);
		}
	}
}

int FindMajority () {
	for (const auto& it : map) {
		if (it.second > (map.size () / 2)) {
			return it.first;
		}
	}

	return INT_MIN;
}

int main (int argc, char** argv) {
	CountElements (input);
	int result = FindMajority ();

	string output = (result != INT_MIN ? to_string(result) : "Error: Majority Element not found");

	cout << "Given the array: [";
	for (int i = 0; i < input.size (); i++) {
		cout << input[i] << ",";
	}
	cout << "]\nThe Majority Element is: " << output << endl;

	return 0;
}