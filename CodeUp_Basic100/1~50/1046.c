#include <stdio.h>
#include <stdlib.h>


int main(void)
{
    long a, b, c;
    scanf("%ld %ld %ld", &a, &b, &c);
    printf("%ld\n%.1f", a+b+c, (float)(a+b+c)/3);
    return 0;
}