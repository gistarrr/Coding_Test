char* solution(int a, int b) 
{
    // 리턴할 값은 메모리를 동적 할당해주세요.
    char *answer = (char*)malloc(4*sizeof(char));
    int date=b-1;
    char *arr[]={"FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};
    int mdays[12]={31, 29, 31, 30, 31, 30, 31, 31 , 30, 31, 30, 31};
    for(int i=0; i<a-1;i++)
        date += mdays[i];
    answer = arr[date%7];

    return answer;
}

/*
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int a, int b) {
    // 리턴할 값은 메모리를 동적 할당해주세요.
    char* answer = (char*)malloc(4*sizeof(char));
    int date=b-1;
    char arr[][4]={"FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};
    int mdays[12]={31, 29, 31, 30, 31, 30, 31, 31 , 30, 31, 30, 31};
    
    for(int i=0; i<a-1;i++)
        date += mdays[i];
    
    strcpy(answer, arr[date%7]);
     
    return answer;
}
*/ 