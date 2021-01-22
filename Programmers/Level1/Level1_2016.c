char* solution(int a, int b) 
{
    // 리턴할 값은 메모리를 동적 할당해주세요.
    char* answer = (char*)malloc(4*sizeof(char));
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

/*
-실수-
char* solution1(int a, int b)
{
	char* answer = (char*)malloc(4 * sizeof(char));
	int date = b - 1;
	char arr[][4] = { "FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU" };		// static 변수로 선언하면 오류 X
	int mdays[12] = { 31, 29, 31, 30, 31, 30, 31, 31 , 30, 31, 30, 31 };
	for (int i = 0; i < a - 1; i++)
		date += mdays[i];
	answer = arr[date % 7];

	return answer;
} // 오류 원인 : arr[][4] 변수는 지역 변수여서 함수가 끝나면 사라지기 때문에 반환한 값을 출력하면 엉뚱한 값이 나오게 된다.
*/