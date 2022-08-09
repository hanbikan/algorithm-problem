#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

void doFloydWarshall(int** graph, int n) {
	int i, j, k;
	for (k = 1; k < n + 1; k++) {
		for (i = 1; i < n + 1; i++) {
			for (j = 1; j < n + 1; j++) {
				if (graph[i][k] != 0 && graph[k][j] != 0)
					graph[i][j] = graph[i][k] + graph[k][j];
			}
		}
	}
}

int main() {
	int i, j;
	
	int n, k;
	scanf("%d %d", &n, &k);

	int** graph = (int**)malloc(sizeof(int*) * (n+1));
	for (i = 1; i < n + 1; i++) {
		graph[i] = (int*)malloc(sizeof(int) * (n + 1));
		for (j = 1; j < n + 1; j++) graph[i][j] = 0;
	}

	for (i = 0; i < k; i++) {
		int a, b;
		scanf("%d %d", &a, &b);

		graph[a][b] = 1;
	}

	doFloydWarshall(graph, n);

	int s;
	scanf("%d", &s);
	for (i = 0; i < s; i++) {
		int a, b;
		scanf("%d %d", &a, &b);

		if (graph[a][b] != 0) printf("-1\n");
		else if (graph[b][a] != 0) printf("1\n");
		else printf("0\n");
	}

	for (i = 1; i < n + 1; i++) free(graph[i]);
	free(graph);

	return 0;
}