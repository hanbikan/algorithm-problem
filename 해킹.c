#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)
#define INF 10000001

typedef struct Node {
	int val;
	struct Node* next;
} Node;

typedef struct Vertex{
	Node* header;
	int hIndex;
	int dist;
} Vertex;

typedef struct Edge {
	int a, b, s;
} Edge;

typedef struct Metadata {
	int n, d, c;
	Vertex** vertices;
	Edge** edges;
} Metadata;

typedef struct Pair {
	int vIndex, dist;
} Pair;

typedef struct PriortyQueue {
	Pair** data;
	int count;
} PriortyQueue;

int main() {
	int i;

	int t;
	scanf("%d", &t);

	for (; t > 0;t--) {
		int n, d, c;
		scanf("%d %d %d", &n, &d, &c);

		Metadata* mt = (Metadata*)malloc(sizeof(Metadata));
		mt->n = n; mt->d = d; mt->c = c;

		// 정점 초기화
		mt->vertices = (Vertex**)malloc(sizeof(Vertex*) * (n + 1));
		for (i = 1; i < n + 1; i++) mt->vertices[i] = getVertex(i);

		// 간선 초기화
		mt->edges = (Edge**)malloc(sizeof(Edge*) * d);
		for (i = 0; i < d; i++) {
			int a, b, s;
			scanf("%d %d %d", &a, &b, &s);

			mt->edges[i] = getEdge(a, b, s);
			addEdgeToVertex(i, mt->vertices[b]);
		}

		doDijkstra(mt);

		freeGraph(mt);
	}

	return 0;
}

Node* getNode(int val) {
	Node* res = (Node*)malloc(sizeof(Node));
	res->val = val; res->next = NULL;
	return res;
}

Vertex* getVertex(int hIndex) {
	Vertex* res = (Vertex*)malloc(sizeof(Vertex));
	res->hIndex = hIndex; res->dist = INF; res->header = getNode(NULL);
	return res;
}

Edge* getEdge(int a, int b, int s) {
	Edge* res = (Edge*)malloc(sizeof(Edge));
	res->a = a; res->b = b; res->s = s;
	return res;
}

void addEdgeToVertex(int eIndex, Vertex* vertex) {
	Node* newNode = getNode(eIndex);
	Node* next = vertex->header->next;
	vertex->header->next = newNode;
	newNode->next = next;
}

void doDijkstra(Metadata* mt) {
	int i;

	// 우선순위큐 초기화
	PriortyQueue* pq = (PriortyQueue*)malloc(sizeof(PriortyQueue));
	pq->count = mt->n;
	pq->data = (Pair**)malloc(sizeof(Pair*) * (mt->n + 1));
	for (i = 1; i < mt->n + 1; i++) {
		pq->data[i] = (Pair*)malloc(sizeof(Pair));
		pq->data[i]->dist = INF;
		pq->data[i]->vIndex = i;
	}
	replaceKey(mt, pq, mt->c, 0);

	mt->vertices[mt->c]->dist = 0;

	while (pq->count > 0) {
		Pair popped = pop(mt, pq);
		int vIndex = popped.vIndex;
		int dist = popped.dist;

		Node* cur = mt->vertices[vIndex]->header->next;
		while (cur) {
			Edge* edge = mt->edges[cur->val];
			int adj = getAdjacentVertexIndex(vIndex, edge);

			if (mt->vertices[adj]->dist > dist + edge->s) {
				mt->vertices[adj]->dist = dist + edge->s;
				replaceKey(mt, pq, mt->vertices[adj]->hIndex, mt->vertices[adj]->dist);
			}

			cur = cur->next;
		}
	}

	int count = 0;
	int maxDist = 0;
	for (i = 1; i < mt->n + 1; i++) {
		if (mt->vertices[i]->dist != INF) {
			if (maxDist < mt->vertices[i]->dist) maxDist = mt->vertices[i]->dist;
			count += 1;
		}
	}

	printf("%d %d\n", count, maxDist);

	// Free
	for (i = 1; i < mt->n + 1; i++) free(pq->data[i]);
	free(pq->data);
	free(pq);
}

void replaceKey(Metadata* mt, PriortyQueue* pq, int index, int val) {
	pq->data[index]->dist = val;
	upheap(mt, pq, index);
}

void upheap(Metadata* mt, PriortyQueue* pq, int index) {
	if (index <= 1) return;

	int parent = index / 2;
	if (pq->data[parent]->dist <= pq->data[index]->dist) return;

	swapItems(mt, pq, parent, index);
	upheap(mt, pq, parent);
}

void swapItems(Metadata* mt, PriortyQueue* pq, int index1, int index2) {
	mt->vertices[pq->data[index1]->vIndex]->hIndex = index2;
	mt->vertices[pq->data[index2]->vIndex]->hIndex = index1;

	Pair* tmp = pq->data[index1];
	pq->data[index1] = pq->data[index2];
	pq->data[index2] = tmp;
}


Pair pop(Metadata* mt, PriortyQueue* pq) {
	Pair res = *pq->data[1];
	pq->data[1]->dist = INF;
	swapItems(mt, pq, 1, pq->count);
	downheap(mt, pq, 1);
	pq->count -= 1;

	return res;
}

void downheap(Metadata* mt, PriortyQueue* pq, int index) {
	if (index * 2 > pq->count) return;

	int child = index * 2;
	if (child + 1 <= pq->count && pq->data[child]->dist > pq->data[child + 1]->dist)
		child++;

	if (pq->data[index]->dist <= pq->data[child]->dist) return;

	swapItems(mt, pq, index, child);
	downheap(mt, pq, child);
}


int getAdjacentVertexIndex(int vIndex, Edge* edge) {
	int res = edge->a;
	if (res == vIndex) res = edge->b;
	return res;
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

	for (i = 0; i < mt->d; i++) free(mt->edges[i]);
	free(mt->edges);

	free(mt);
}