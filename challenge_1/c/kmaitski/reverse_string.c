#include <string.h>
#include <stdio.h>

void reverse_string(char *str)
{
	int x = strlen(str);
	while (x >= 0)
	{
		printf("%c", str[x]);
		x--;
	}
}
