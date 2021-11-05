#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

typedef struct Node {
	int var;
	int index;
	struct Node* next;
}Node;

typedef struct Stack {
	int size;
	Node* top;
}Stack;

Node* getNode(int var, int index) {
	Node* res = malloc(sizeof(Node));
	res->next = NULL;
	res->var = var;
	res->index = index;
	return res;
}

void push(Stack* stack, int var, int index) { 
	Node* newNode = getNode(var, index);
	newNode->next = stack->top;
	stack->top = newNode;
	stack->size += 1;
}

Node pop(Stack* stack) {
	Node res;
	res.index = -1;
	res.var = -1;
	res.next = NULL;
	if (stack->size <= 0) return res;

	Node* next = stack->top->next;
	res.var = stack->top->var;
	res.index = stack->top->index;

	free(stack->top);
	stack->top = next;
	stack->size -= 1;

	return res;
}

int main() {
	int N;
	scanf("%d", &N);

	int i;
	int* res = malloc(sizeof(int) * N);
	
	Stack* stack = malloc(sizeof(Stack));
	stack->size = 0;
	stack->top = NULL;

	int* nums = malloc(sizeof(int) * N);
	for (i = 0; i < N; i++) {
		res[i] = -1;
		scanf("%d", &nums[i]);
		
		while (stack->size >= 1 && stack->top->var < nums[i]) {
			Node popped = pop(stack);
			res[popped.index] = i;
		}

		push(stack, nums[i], i);
	}

	for (i = 0; i < N; i++) {
		if (res[i] == -1) printf("-1 ");
		else printf("%d ", nums[res[i]]);
	}

	free(res);
	free(nums);

	return 0;
}