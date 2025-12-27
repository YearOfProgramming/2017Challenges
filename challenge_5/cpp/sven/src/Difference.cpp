#include <iostream>
#include <string>
#include <algorithm>

int main(int argc, char* argv[])
{
	std::string normalString = argv[1];
	std::string extraChar = argv[2];
	auto it = std::find_if(extraChar.begin(), extraChar.end(), [&normalString](char c) 
	{
		return normalString.find(c) == std::string::npos;
	});

	std::cout << *it << std::endl;


}

