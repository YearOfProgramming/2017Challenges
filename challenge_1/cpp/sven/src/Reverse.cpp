#include <iostream>
#include <string>

int main(int argc, char* argv[])
{
	for (int i = argc - 1; i > 0; --i)
	{
		std::string word = argv[i];
		for (std::string::reverse_iterator rit = word.rbegin(); rit != word.rend(); ++rit)
			std::cout << *rit;
		std::cout << " ";
	}
	std::cout << std::endl;
	return 0;
}