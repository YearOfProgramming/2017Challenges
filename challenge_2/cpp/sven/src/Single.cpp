#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>

int main(int argc, char* argv[])
{
	std::unordered_map<std::string, bool> map;
	for (int i =1; i < argc; ++i)
	{
		std::string el = argv[i];
		if (map.find(el) == map.cend())
		{
			map[el] = true;
		}
		else
		{
			map[el] = false;
		}
	}
	std::cout << std::find_if(map.cbegin(), map.cend(), [](const std::unordered_map<std::string, bool>::value_type& vt) { return vt.second; })->first << std::endl;
}