#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
// �Ķ���ͷ� �־����� ���ڿ��� const�� �־����ϴ�. �����Ϸ��� ���ڿ��� �����ؼ� ����ϼ���.
char* solution(const char* number, int k) {
    // return ���� malloc �� ���� �Ҵ��� ������ּ���. �Ҵ� ���̴� ��Ȳ�� �°� �������ּ���.
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