#include <stdio.h>

void swap(int *n1, int *n2) {
	int temp = *n1;
	*n1 = *n2;
	*n2 = temp;
}

void bubbleSort(int vectorEntrada[], int n) {
	int i, j;

	for(i = 0; i < n-1; ++i) {
		for(j = 0; j < n-i-1; ++j) {
			if(vectorEntrada[j] > vectorEntrada[j+1]) {
				swap(&vectorEntrada[j], &vectorEntrada[j+1]);
			}
		}
	}
}

void print(int vectorEntrada[], int n) {
	int i;
	for(i = 0; i < n-1; ++i) {
		printf("%d  , ", vectorEntrada[i]);
	}
	printf("\nFin de Ordenamiento");
}

int main() {
	int vectorEntrada[] = {23, 44, 576, -1, -23, 4, 98, 502, 1, 32, 4, 5, 18};
	int n = sizeof(vectorEntrada) / sizeof(vectorEntrada[0]);

	bubbleSort(vectorEntrada, n);
	print(vectorEntrada, n);
	printf("\n");

	return 0;
}
