#include <iostream>
#include <string>
#include <algorithm>

int main(int argc, char* argv[])
{
	int rangeBegin = std::stoi(argv[1]);
	int rangeEnd = rangeBegin;
	for (int i = 2; i < argc; ++i)
	{
		if (rangeEnd + 1 == std::stoi(argv[i]))
		{
			rangeEnd++;
		}
		else
		{
			std::cout << rangeBegin << "->" << rangeEnd << std::endl;
			rangeBegin = std::stoi(argv[i]);
			rangeEnd = rangeBegin;
		}
	}
	std::cout << rangeBegin << "->" << rangeEnd << std::endl;
}

