#include <stdio.h>
#include <stdlib.h>


int main(void)
{
    char a[21];
    int len;
    scanf("%s", a);
    len=strlen(a);
    for(int i=0;i<len;i++)
        printf("\'%c\'\n", a[i]);

    return 0;
}