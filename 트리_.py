import sys
input = sys.stdin.readline

def f(preorderStart, preorderEnd):      
    if preorderStart >= preorderEnd:
        return

    global preorder, inorder, preorderIndex
    parent = preorder[preorderIndex] 
    preorderIndex += 1

    inorderParentIndex = inorder.index(parent)
    f(preorderStart, inorderParentIndex)
    f(inorderParentIndex+1, preorderEnd)
    print(parent, end=" ")

def solution():
    global preorder, inorder, preorderIndex

    T = int(input())
    for _ in range(T):
        preorderIndex = 0

        n = int(input())
        preorder = list(map(int, input().split()))
        inorder = list(map(int, input().split()))      

        f(0, n)
        print()

if __name__ == '__main__':
    solution()