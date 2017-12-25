#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>

int main(int argc, char* argv[])
{
	std::unordered_map<std::string, int> map;
	std::pair<std::string, int> majority(argv[1], 1);

	for (int i = 1; i < argc; ++i)
	{
		map[argv[i]]++;
		if(map[argv[i]] > majority.second)
		{
			majority = std::pair<std::string, int>(argv[i], map[argv[i]]);
		}
	}
	std::cout << majority.first << std::endl;
}