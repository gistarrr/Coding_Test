#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* number, int k) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(sizeof(char)*1000000);
    int len = strlen(number);
    int i, j=0, cnt=0;
    int max, max_index, remove = k;
    int start_index=0;

    while(cnt<k){
        if(j >= len-k )
        {            
            break;
        }        
        max=number[start_index], max_index=start_index;
        for(i=start_index+1; i<=start_index+remove;i++)
        {
            if(max<number[i]){
                max=number[i];
                max_index = i;
            }
        }
        answer[j++]=max;
        cnt = max_index - start_index;
        start_index = max_index+1;
        remove -=cnt;
    }

    if(j < len-k)
    { 
        strcpy(&answer[j], &number[j]);
    }

    return answer;

}