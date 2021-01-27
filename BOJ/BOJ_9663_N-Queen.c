#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int pos[15];
int flag[15] = { 0 };
int flag_a[28] = { 0 };	// i+j 가 일정
int flag_b[28] = { 0 }; // i-j+14 가 일정
int n;
int cnt=0;

int Queen(int i)
{
	int j;
	for (j = 0; j < n; j++)
	{
		if (!flag[j] && !flag_a[i+j] && !flag_b[i-j+n-1]) {
			pos[i] = j;			
			if (i == n-1)
				cnt++;
			else {
				flag[j] = flag_a[i + j] = flag_b[i - j + n - 1] = 1;
				Queen(i + 1);
				flag[j] = flag_a[i + j] = flag_b[i - j + n - 1] = 0;
			}
		}

	}

}


int main(void)
{
	
	scanf("%d", &n);
	Queen(0);
	printf("%d", cnt);

	return 0;
}