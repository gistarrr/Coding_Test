#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


// prices_len�� �迭 prices�� �����Դϴ�.
int* solution(int prices[], size_t prices_len) {
    // return ���� malloc �� ���� �Ҵ��� ������ּ���. �Ҵ� ���̴� ��Ȳ�� �°� �������ּ���.
    int* answer = (int*)malloc(sizeof(int)*prices_len);
    int i, j;
    for(i=0;i<prices_len;i++)
    {
        for(j=i+1;j<prices_len;j++)
        {
            if(prices[i]>prices[j]){
                j++;
                break;
            }

        }
        answer[i]=j-1-i;
    }   
    return answer;
}