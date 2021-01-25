#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    long long int temp, a=0, b=1;
    if(n==1)
    {
        answer = 1;
    }
    for(int i=0;i<n-1;i++)
    {
        temp = a%1234567 + b%1234567;
        a = b;
        b = temp;
    }
    answer = temp%1234567;
    return answer;
}

// int 계산 범위를 생각해서 풀 것!