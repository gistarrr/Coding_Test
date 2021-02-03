#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arr_len은 배열 arr의 길이입니다.
int solution(int arr[], size_t arr_len) {
    int answer = 0;
    answer=arr[0];
    for(int i=1; i<arr_len; i++)
    {
        answer=lcm(answer,arr[i]);
    }
    
    return answer;
}
int gcd(int x, int y)
{
    if(x==0){
        return y;
    }else{
        return gcd(y%x, x);
    }
}
int lcm(int x, int y)
{
    return x*y/gcd(x, y);
    
}