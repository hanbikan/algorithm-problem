#include <stdio.h>
#include <stdlib.h>

int *parents;

int findParent(int x)
{
    if (parents[x] == x)
        return x;

    parents[x] = findParent(parents[x]);
    return parents[x];
}

void unionSets(int x, int y)
{
    int parentX = findParent(x);
    int parentY = findParent(y);

    if (parentX < parentY)
        parents[parentX] = parentY;
    else
        parents[parentY] = parentX;
}

int main()
{
    int i, j;

    int N;
    scanf("%d", &N);

    // parents 초기화
    parents = malloc(sizeof(int) * N);
    for (i = 0; i < N; i++)
        parents[i] = i;

    int M;
    scanf("%d", &M);

    int input;
    for (i = 0; i < N; i++)
    {
        for (j = 0; j < N; j++)
        {
            scanf("%d", &input);

            if (input == 1)
                unionSets(i, j);
        }
    }

    // 여행 계획 입력
    int isPossible = 0;
    scanf("%d", &input);
    int prevParent = findParent(input - 1);
    for (i = 1; i < M; i++)
    {
        scanf("%d", &input);

        if (findParent(input - 1) != prevParent)
        {
            isPossible = -1;
            break;
        }
    }

    // 출력
    if (isPossible == 0)
        printf("YES");
    else
        printf("NO");

    return 0;
}