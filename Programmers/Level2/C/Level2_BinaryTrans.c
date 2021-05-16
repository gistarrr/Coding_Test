#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* exchange(int length) {	
	char *result = (char*)malloc(sizeof(char) *length);
	int i = 0;
	while (length > 0) {
		if (length % 2 == 1)
			result[i++] = '1';
		else
			result[i++] = '0';
		length /= 2;
	}
	for (int k = 0; k < i / 2; k++) {
		char temp = result[k];
		result[k] = result[i - k - 1];
		result[i - k - 1] = temp;
	}
	result[i] = '\0';
	return result;
}
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int* solution(const char* s) {
	// return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
	int* answer = (int*)malloc(sizeof(int) * 2);
	char* copy = (char*)malloc(sizeof(char) * 150000);
	int num, zero=0, count = 0;
	strcpy(copy, s);
	while (strlen(copy) != 1){
		num = 0;
		int len = strlen(copy);
		for (int j = 0; j < len; j++) {
			if (copy[j] == '1') {
				num++;
			}
			else {
				zero++;
			}			
		}
		strcpy(copy, exchange(num));
		count++;
	}
	answer[0] = count;
	answer[1] = zero;

	return answer;
}