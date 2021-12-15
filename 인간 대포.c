#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#pragma warning(disable:4996)
#define INF 101

typedef struct Position {
	double x, y;
} Position;

typedef struct Metadata {
	int n;
	Position* obj;
	double** graph;
} Metadata;

typedef struct Pair {
	int vIndex;
	double dist;
} Pair;

typedef struct PriortyQueue {
	int count;
	Pair* data;
} PriortyQueue;

Position scanPosition() {
	Position res;
	scanf("%lf %lf", &res.x, &res.y);
	return res;
}

double getDistance(Position p1, Position p2) {
	return sqrt(pow(p1.x - p2.x, 2) + pow(p1.y - p2.y, 2));
}

void swapItems(PriortyQueue* pq, int* locator, int index1, int index2) {
	locator[pq->data[index1].vIndex] = index2;
	locator[pq->data[index2].vIndex] = index1;

	Pair tmp = pq->data[index1];
	pq->data[index1] = pq->data[index2];
	pq->data[index2] = tmp;
}

void upheap(PriortyQueue* pq, int* locator, int index) {
	if (index <= 1) return;

	int parent = index / 2;
	if (pq->data[parent].dist <= pq->data[index].dist) return;

	swapItems(pq, locator, parent, index);
	upheap(pq, locator, parent);
}

void replaceKey(PriortyQueue* pq, int* locator, int index, double dist) {
	pq->data[index].dist = dist;
	upheap(pq, locator, index);
}

void downheap(PriortyQueue* pq, int* locator, int index) {
	if (index * 2 > pq->count) return;

	int child = index * 2;
	if (child + 1 <= pq->count && pq->data[child].dist > pq->data[child + 1].dist)
		child += 1;

	if (pq->data[index].dist <= pq->data[child].dist) return;

	swapItems(pq, locator, index, child);
	downheap(pq, locator, child);
}

Pair pop(PriortyQueue* pq, int* locator) {
	Pair res = pq->data[1];

	pq->data[1].dist = INF;
	swapItems(pq, locator, 1, pq->count);
	downheap(pq, locator, 1);
	pq->count -= 1;

	return res;
}

void doDijkstra(Metadata* mt) {
	int i;
	// dist
	double* dist = (double*)malloc(sizeof(double)*(mt->n+2));
	for (i = 1; i < mt->n + 2; i++) dist[i] = INF;
	dist[0] = 0;

	// 우선순위큐 초기화
	PriortyQueue* pq = (PriortyQueue*)malloc(sizeof(PriortyQueue));
	pq->count = mt->n + 2;
	pq->data = (Pair*)malloc(sizeof(Pair) * (mt->n + 3)); // 주의: 1-indexing
	int* locator = (int*)malloc(sizeof(int) * (mt->n + 2));
	for (i = 1; i < mt->n + 3; i++) {
		pq->data[i].dist = INF;
		pq->data[i].vIndex = i-1;
		locator[i - 1] = i;
	}
	replaceKey(pq, locator, locator[0], 0);

	// 다익스트라
	while (pq->count > 0) {
		Pair popped = pop(pq, locator);
		int vIndex = popped.vIndex;
		double d = popped.dist;

		for (i = 0; i < mt->n + 2; i++) {
			if (i != vIndex && dist[i] > d + mt->graph[vIndex][i]) {
				dist[i] = d + mt->graph[vIndex][i];
				replaceKey(pq, locator, locator[i], dist[i]);
			}
		}
	}
	
	printf("%f", dist[1]);

	// Free
	free(locator);
	free(pq->data);
	free(pq);
	free(dist);
}

int main() {
	int i, j;

	Metadata* mt = (Metadata*)malloc(sizeof(Metadata));

	Position a = scanPosition();
	Position b = scanPosition();

	scanf("%d", &mt->n);
	mt->obj = (Position*)malloc(sizeof(Position) * (mt->n+2));
	mt->obj[0] = a; mt->obj[1] = b;

	for (i = 2; i < mt->n+2; i++) {
		mt->obj[i] = scanPosition();
	}

	mt->graph = (double**)malloc(sizeof(double*) * (mt->n + 2));
	for (i = 0; i < 2; i++) {
		mt->graph[i] = (double*)malloc(sizeof(double)*(mt->n+2));

		for (j = 0; j < mt->n + 2; j++) {
			if (i == j) mt->graph[i][j] = 0;
			else {
				double dist = getDistance(mt->obj[i], mt->obj[j]);
				mt->graph[i][j] = dist / 5;
			}
			
		}
	}
	for (i = 2; i < mt->n+2; i++) {
		mt->graph[i] = (double*)malloc(sizeof(double) * (mt->n + 2));

		for (j = 0; j < mt->n + 2; j++) {
			if (i == j) mt->graph[i][j] = 0;
			else {
				double dist = getDistance(mt->obj[i], mt->obj[j]) - 50;
				if (dist < 0) dist *= -1;
				mt->graph[i][j] =  dist / 5 + 2;
			}
		}
	}

	doDijkstra(mt);

	// Free
	free(mt->obj);
	free(mt);

	return 0;
}