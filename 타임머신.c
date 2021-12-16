#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)
#define INF 5000001

typedef struct Node {
	int val;
	struct Node* next;
} Node;

typedef struct Vertex {
	Node* header;
} Vertex;

typedef struct Edge {
	int a, b, w;
} Edge;

typedef struct Metadata {
	int n, m;
	Vertex** vertices;
	Edge** edges;
} Metadata;

Node* getNode(int val) {
	Node* res = (Node*)malloc(sizeof(Node));
	res->val = val; res->next = NULL;
	return res;
}

Vertex* getVertex() {
	Vertex* res = (Vertex*)malloc(sizeof(Vertex));
	res->header = getNode(NULL);
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

int getAdjacentVertexIndex(Edge* edge, int vIndex) {
	int res = edge->a;
	if (res == vIndex) res = edge->b;
	return res;
}

void doBellmanFord(Metadata* mt) {
	int i, j;

	long long* dist = (long long*)malloc(sizeof(long long) * (mt->n + 1));
	for (i = 1; i < mt->n + 1; i++) dist[i] = INF;
	dist[1] = 0;

	for (j = 0; j < mt->n; j++) {
		for (i = 1; i < mt->n + 1; i++) {
			if (dist[i] == INF) continue;

			Node* cur = mt->vertices[i]->header->next;
			while (cur) {
				Edge* edge = mt->edges[cur->val];
				int adj = getAdjacentVertexIndex(edge, i);

				if (dist[adj] > dist[i] + edge->w) {
					dist[adj] = dist[i] + edge->w;

					if (j == mt->n - 1) {
						printf("-1");
						return;
					}
				}

				cur = cur->next;
			}
		}
	}

	// 도시에 대한 최단경로 출력
	for (i = 2; i < mt->n + 1; i++) {
		if (dist[i] == INF) printf("-1\n");
		else printf("%lld\n", dist[i]);
	}
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

	for (i = 0; i < mt->m; i++) free(mt->edges[i]);
	free(mt->edges);

	free(mt);
}

int main() {
	int i;

	Metadata* mt = (Metadata*)malloc(sizeof(Metadata));
	scanf("%d %d", &mt->n, &mt->m);

	mt->vertices = (Vertex**)malloc(sizeof(Vertex*) * (mt->n + 1));
	for (i = 1; i < mt->n + 1; i++) mt->vertices[i] = getVertex();

	mt->edges = (Edge**)malloc(sizeof(Edge*) * mt->m);
	for (i = 0; i < mt->m; i++) {
		int a, b, w;
		scanf("%d %d %d", &a, &b, &w);
		mt->edges[i] = getEdge(a, b, w);

		addEdgeToVertex(i, mt->vertices[a]);
	}

	doBellmanFord(mt);

	freeGraph(mt);

	return 0;
}