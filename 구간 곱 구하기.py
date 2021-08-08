import sys
input = sys.stdin.readline
DIV = 1000000007


def initializeSegmentTree(index, start, end):
    if start == end:
        tree[index] = nums[start]
    else:
        mid = (start + end)//2
        tree[index] = initializeSegmentTree(
            index*2, start, mid) * initializeSegmentTree(index*2+1, mid+1, end) % DIV

    return tree[index]


def updateNode(index, target, value, start, end):
    # 범위를 벗어남
    if target < start or end < target:
        return

    # 리프 노드
    if start == end:
        tree[index] = value
        return

    mid = (start + end)//2
    updateNode(index*2, target, value, start, mid)
    updateNode(index*2+1, target, value, mid+1, end)

    tree[index] = tree[index*2]*tree[index*2+1] % DIV


def getSum(index, range, start, end):
    # 범위를 벗어남
    if range[1] < start or end < range[0]:
        return 1

    # range <= start, end <= range[1]
    if range[0] <= start and end <= range[1]:
        return tree[index]

    mid = (start + end)//2
    return getSum(index*2, range, start, mid) * getSum(index*2+1, range, mid+1, end) % DIV


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    nums = [-1] + list(int(input()) for _ in range(N))

    # Initialize segment tree
    tree = [0]*(N*4)
    initializeSegmentTree(1, 1, N)

    for _ in range(M + K):
        a, b, c = map(int, input().split())
        if a == 1:
            # xchg
            updateNode(1, b, c, 1, N)
            nums[b] = c
        else:
            # Print sum
            sop = getSum(1, (b, c), 1, N)
            print(sop)
