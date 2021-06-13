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
    int i;

    int n, m;
    scanf("%d %d", &n, &m);

    // parents 초기화
    parents = malloc(sizeof(int) * (n + 1));

    for (i = 1; i < n + 1; i++)
        parents[i] = i;

    // 연산 수행
    int order, a, b;
    int parentA, parentB;
    for (i = 0; i < m; i++)
    {
        scanf("%d %d %d", &order, &a, &b);

        if (order == 0)
            unionSets(a, b);
        else if (order == 1)
        {
            parentA = findParent(a);
            parentB = findParent(b);

            if (parentA == parentB)
                printf("YES\n");
            else
                printf("NO\n");
        }
    }

    return 0;
}