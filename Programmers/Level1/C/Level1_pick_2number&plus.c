#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// numbers_len은 배열 numbers의 길이입니다.
int* solution(int numbers[], size_t numbers_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc((numbers_len*numbers_len-1)/2*sizeof(int));
    int i,j,k,temp, ptr=0;
    for(i=0; i<numbers_len-1;i++)
    {
        for(j=i+1; j<numbers_len;j++)
        {
            int flag=0;
            temp=numbers[i]+numbers[j];
            for(k=0;k<ptr;k++)
                if(answer[k]==temp)
                    flag=1;
            if(!flag)
                answer[ptr++]=temp;
        }
    }
    for(i=0;i<ptr-1;i++)
    {
        for(j=i+1;j<ptr;j++)
        {
            if(answer[i]>answer[j])
            {
                temp=answer[i];
                answer[i]=answer[j];
                answer[j]=temp;
            }
        }
    }

    return answer;
}