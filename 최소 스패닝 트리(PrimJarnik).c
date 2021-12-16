#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)
#define INF 10000000001

typedef struct Node {
	int val;
	struct Node* next;
} Node;

typedef struct Vertex {
	Node* header;
	int hIndex;
} Vertex;

typedef struct Edge {
	int a, b, w;
} Edge;

typedef struct Metadata {
	int n, k;
	Vertex** vertices;
	Edge** edges;
} Metadata;

typedef struct Pair {
	int vIndex, dist;
} Pair;

typedef struct PriortyQueue {
	Pair* data;
	int count;
} PriortyQueue;

Node* getNode(int val) {
	Node* res = (Node*)malloc(sizeof(Node));
	res->val = val; res->next = NULL;
	return res;
}

Vertex* getVertex(int hIndex) {
	Vertex* res = (Vertex*)malloc(sizeof(Vertex));
	res->hIndex = hIndex;  res->header = getNode(NULL);
	return res;
}

Edge* getEdge(int a, int b, int w) {
	Edge* res = (Edge*)malloc(sizeof(Edge));
	res->a = a; res->b = b; res->w = w;
	return res;
}

void addEdgeToVertex(int eIndex, Vertex* vertex) {
	Node* newNode = getNode(eIndex);
	Node* next = vertex->header->next;
	vertex->header->next = newNode;
	newNode->next = next;
}

void swapItems(Metadata* mt, PriortyQueue* pq, int index1, int index2) {
	mt->vertices[pq->data[index1].vIndex]->hIndex = index2;
	mt->vertices[pq->data[index2].vIndex]->hIndex = index1;

	Pair tmp = pq->data[index1];
	pq->data[index1] = pq->data[index2];
	pq->data[index2] = tmp;
}

void upheap(Metadata* mt, PriortyQueue* pq, int index) {
	if (index <= 1) return;

	int parent = index / 2;
	if (pq->data[parent].dist <= pq->data[index].dist) return;

	swapItems(mt, pq, index, parent);
	upheap(mt, pq, parent);
}

void replaceKey(Metadata* mt, PriortyQueue* pq, int index, int dist) {
	pq->data[index].dist = dist;
	upheap(mt, pq, index);
}

void downheap(Metadata* mt, PriortyQueue* pq, int index) {
	if (index*2 > pq->count) return;

	int child = index * 2;
	if (child + 1 <= pq->count && pq->data[child].dist > pq->data[child + 1].dist)
		child += 1;

	if (pq->data[index].dist <= pq->data[child].dist) return;

	swapItems(mt, pq, child, index);
	downheap(mt, pq, child);
}

Pair getPair(Metadata* mt, PriortyQueue* pq) {
	Pair res = pq->data[1];

	pq->data[1].dist = INF;
	swapItems(mt, pq, 1, pq->count);
	downheap(mt, pq, 1);
	pq->count -= 1;

	return res;
}

int getAdjacentVertexIndex(Edge* edge, int vIndex) {
	int res = edge->a;
	if (res == vIndex) res = edge->b;
	return res;
}

void doPrimJarnik(Metadata* mt) {
	int i;
	
	// dist 초기화
	int* dist = (int*)malloc(sizeof(int) * (mt->n + 1));
	for (i = 1; i < mt->n + 1; i++) dist[i] = INF;
	dist[1] = 0;

	// isVisited 초기화
	int* isVisited = (int*)malloc(sizeof(int) * (mt->n + 1));
	for (i = 1; i < mt->n + 1; i++) isVisited[i] = 0;

	// pq 초기화
	PriortyQueue* pq = (PriortyQueue*)malloc(sizeof(PriortyQueue));
	pq->data = (Pair*)malloc(sizeof(Pair) * (mt->n + 1));
	for (i = 1; i < mt->n + 1; i++) {
		pq->data[i].dist = INF;
		pq->data[i].vIndex = i;
	}
	pq->count = mt->n;
	replaceKey(mt, pq, 1, 0);

	// PrimJarnik
	while (pq->count > 0) {
		int vIndex = getPair(mt, pq).vIndex;
		isVisited[vIndex] = 1;

		Node* cur = mt->vertices[vIndex]->header->next;
		while (cur) {
			Edge* edge = mt->edges[cur->val];
			int adj = getAdjacentVertexIndex(edge, vIndex);

			if (isVisited[adj] == 0 && dist[adj] > edge->w) {
				dist[adj] = edge->w;
				replaceKey(mt, pq, mt->vertices[adj]->hIndex, dist[adj]);
			}

			cur = cur->next;
		}
	}

	// 출력
	long long sum = 0;
	for (i = 2; i < mt->n + 1; i++) sum += dist[i];
	printf("%lld", sum);

	// Free
	free(pq);
	free(isVisited);
	free(dist);
}

void freeGraph(Metadata* mt) {
	int i;
	for (i = 1; i < mt->n + 1; i++) {
		Node* cur = mt->vertices[i]->header;
		while (cur) {
			Node* next = cur->next;
			free(cur);
			cur = next;
		}
		free(mt->vertices[i]);
	}
	free(mt->vertices);

	for (i = 0; i < mt->k; i++) free(mt->edges[i]);
	free(mt->edges);

	free(mt);
}

int main() {
	int i;

	int n, k;
	scanf("%d %d", &n, &k);

	Metadata* mt = (Metadata*)malloc(sizeof(Metadata));
	mt->n = n; mt->k = k;

	mt->vertices = (Vertex**)malloc(sizeof(Vertex*) * (n + 1));
	for (i = 1; i < n + 1; i++) {
		mt->vertices[i] = getVertex(i);
	}

	mt->edges = (Edge**)malloc(sizeof(Edge*) * k);
	for (i = 0; i < k; i++) {
		int a, b, w;
		scanf("%d %d %d", &a, &b, &w);

		mt->edges[i] = getEdge(a, b, w);
		addEdgeToVertex(i, mt->vertices[a]);
		addEdgeToVertex(i, mt->vertices[b]);
	}

	doPrimJarnik(mt);

	freeGraph(mt);

	return 0;
}