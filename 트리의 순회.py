import sys
sys.setrecursionlimit(500000)
input = sys.stdin.readline


def printPreorder(inorderStartIndex, inorderEndIndex, postorderStartIndex, postorderEndIndex):
    length = inorderEndIndex - inorderStartIndex

    if length == 0:
        return
    elif length == 1:
        print(inorder[inorderStartIndex:inorderEndIndex][0], end=" ")
        return

    root = postorder[postorderEndIndex-1]
    inorderRootIndex = inorderIndices[root]
    leftLength = inorderRootIndex - inorderStartIndex

    print(root, end=" ")
    printPreorder(inorderStartIndex, inorderRootIndex,
                  postorderStartIndex, postorderStartIndex + leftLength)
    printPreorder(inorderRootIndex + 1, inorderEndIndex,
                  postorderStartIndex + leftLength, postorderEndIndex - 1)


if __name__ == '__main__':
    # 입력
    n = int(input())
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))

    # 각 노드의 inorder에서의 인덱스를 저장
    inorderIndices = [-1]*(n+1)
    for i in range(n):
        inorderIndices[inorder[i]] = i

    # 출력
    printPreorder(0, n, 0, n)
