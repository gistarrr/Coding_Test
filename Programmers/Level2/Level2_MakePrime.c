#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// nums_len은 배열 nums의 길이입니다.
int solution(int nums[], size_t nums_len) {
    int answer = 0;
    int temp, flag, n;
    for(int i=0;i<nums_len-2;i++)
    {
        for(int j=i+1;j<nums_len-1;j++)
        {
            for(int k=j+1;k<nums_len;k++)
            {
                flag=0;
                temp=nums[i]+nums[j]+nums[k];
                if(temp%2 == 0)
                    continue;
                else
                {
                    n=temp-2;
                    while(n>1)
                    {
                        if(temp%n == 0)
                        {
                        flag=1;
                        break;
                        }                        
                        n=n-2;
                    }
                    if(flag==0)
                        answer++;
                }

            }
        }
    }
    return answer;
}