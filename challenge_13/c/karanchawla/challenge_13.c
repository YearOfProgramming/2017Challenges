//Karan Chawla
//Challenge 13

#include <stdio.h>
#include <stdlib.h>

int reverse(int x)
{
    int ans = 0;
    while(x != 0)
    {
        ans = ans * 10;
        ans = ans + x%10;
        x = x/10;
    }
    
    return ans;
}


//Driver Program
int main(void)
{
    int num = 1234554321;

    if(reverse(num)==num)
    {
        printf("True");
    }
    else
    {
        printf("False");
    }

    return 0;
}
