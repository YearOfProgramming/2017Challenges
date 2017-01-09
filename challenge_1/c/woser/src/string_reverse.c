#include <stdio.h>
#include <string.h>

void string_reverse(char* string){
	char* start = string;
	char* end = start + strlen(string) - 1;
	char tmp;
	
	while (end > start){
		tmp = *start;
		*start = *end;
		*end = tmp;
		
		++start;
		--end;
	}
}

int main(void){
	char string[] = "Hello!";
	string_reverse(string);
	printf("%s\n", string);
	return 0;
}