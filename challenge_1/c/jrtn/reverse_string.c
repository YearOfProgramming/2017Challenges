#include <string.h>
void inplace_reverse(char *str) {
    size_t len = strlen(str);
    int i;
    for(i = 0; i < len / 2; i++) {
        char temp;
        temp = str[len - 1 - i];
        str[len - 1 - i] = str[i];
        str[i] = temp;
    }
}
