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
// �Ķ���ͷ� �־����� ���ڿ��� const�� �־����ϴ�. �����Ϸ��� ���ڿ��� �����ؼ� ����ϼ���.
int* solution(const char* s) {
	// return ���� malloc �� ���� �Ҵ��� ������ּ���. �Ҵ� ���̴� ��Ȳ�� �°� �������ּ���.
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