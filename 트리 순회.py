import sys
input = sys.stdin.readline


def printWithPreorderTraversal(node):
    if node == '.':
        return

    print(node, end="")
    printWithPreorderTraversal(tree[node][0])
    printWithPreorderTraversal(tree[node][1])


def printWithInorderTraversal(node):
    if node == '.':
        return

    printWithInorderTraversal(tree[node][0])
    print(node, end="")
    printWithInorderTraversal(tree[node][1])


def printWithPostorderTraversal(node):
    if node == '.':
        return

    printWithPostorderTraversal(tree[node][0])
    printWithPostorderTraversal(tree[node][1])
    print(node, end="")


if __name__ == '__main__':
    N = int(input())

    tree = {}
    for _ in range(N):
        v, l, r = map(str, input().split())
        tree[v] = [l, r]

    printWithPreorderTraversal('A')
    print()
    printWithInorderTraversal('A')
    print()
    printWithPostorderTraversal('A')
