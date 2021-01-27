#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int max=0;

int Search_max(int a[], int m, int n)
{
	int temp;
	for (int i = 0; i < n-2; i++)
	{
		for (int j = i + 1; j < n - 1; j++)
		{
			for (int k = j + 1; k < n; k++)
			{
				temp = a[i] + a[j] + a[k];
				if (temp > max && temp <= m)
					max = temp;
			}
		}
	}

	
	return max;

}


int main(void)
{
	int n, m;
	int *arr;
	scanf("%d %d", &n, &m);
	arr = (int *)malloc(sizeof(int)*n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &arr[i]);
	}
	printf("%d", Search_max(arr, m, n));

	return 0;
}