import sys
input = sys.stdin.readline


def update_fenwick_tree(tree, index, value):
    while index < len(tree):
        tree[index] += value
        index += (index & -index)

    return tree


def query_fenwick_tree(tree, index):
    res = 0
    while index > 0:
        res += tree[index]
        index -= (index & -index)

    return res


if __name__ == '__main__':
    N, M, K = map(int, input().split())

    tree = [0]*(N+1)
    nums = [int(input()) for _ in range(N)]
    for i in range(N):
        tree = update_fenwick_tree(tree, i+1, nums[i])

    for _ in range(M + K):
        a, b, c = map(int, input().split())

        if a == 1:
            tree = update_fenwick_tree(tree, b, c - nums[b-1])
            nums[b-1] = c
        elif a == 2:
            print(query_fenwick_tree(tree, c) - query_fenwick_tree(tree, b-1))
