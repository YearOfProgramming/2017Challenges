#include <stdio.h>
char find_the_difference(char * s, char * t) {
    int tSum = 0;
    int sSum = 0;
    int i = 0;
    while(t[i]) {
        tSum += t[i];
        if(s[i]) {
            sSum += s[i];
        }
        i++;
    }

    return (char)(tSum - sSum);
}

int main() {
    char * s = "abcd";
    char * t = "abcde";
    char dif = find_the_difference(s, t);
    printf("'%c'\n", dif);

    char * s1 = "abcd";
    char * t1 = "dcabe";
    char dif1 = find_the_difference(s1, t1);
    printf("'%c'\n", dif1);

    char * s2 = "abcdefghijklmno";
    char * t2 = "abcdefghijklmnop";
    char dif2 = find_the_difference(s2, t2);
    printf("'%c'\n", dif2);

    char * s3 = " ";
    char * t3 = " ";
    char dif3 = find_the_difference(s3, t3);
    printf("'%c'\n", dif3);
    return 0;
}
