#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

vector<string> input = {"2", "3", "4", "2", "3", "5", "4", "6", "4", "6", "9", "10", "9", "8", "7", "8", "10", "7"};
vector<string> extra = {"2", "a", "l", "3", "l", "4", "k", "2", "3", "4", "a", "6", "c", "4", "m", "6", "m", "k", "9", "10", "9", "8", "7", "8", "10", "7"};
map<string, int> table; // First = number/ character, Second = count

// Counts how many times each number/ character appears by placing it in the map or incrementing the count
void CountArray(vector<string> array){
	for(int i = 0; i < array.size(); i++){
		auto it = table.find(array[i]);
		if(it != table.end()){ // If the number/ character is found, increment count
			it->second++;
		} else{
			table.emplace(array[i], 1); // Else add it to the map
		}
	}
}

// Iterate through map to find where the count = 0
string FindSingle(){
	for(auto it = table.begin(); it != table.end(); it++){
		if(it->second == 1){
			return it->first;
		}
	}

	return NULL;
}

int main(int argc, char** argv){
	CountArray(input);
	cout << "The number/ character that appears once is: " << FindSingle() << endl;
	return 0;
}