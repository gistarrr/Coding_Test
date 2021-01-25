#include <stdio.h>
#include <stdlib.h>


int main(void)
{
    long a, b;
    scanf("%ld %ld",&a, &b);
    printf("%d", (a <= b) ? 1 : 0);
    return 0;
}