import sys
input = sys.stdin.readline


def initializeSegmentTree(index, start, end):
    if start == end:
        tree[index] = (nums[start], nums[start])
        return

    mid = (start + end)//2
    initializeSegmentTree(index*2, start, mid)
    initializeSegmentTree(index*2+1, mid+1, end)
    tree[index] = (min(tree[index*2][0], tree[index*2+1][0]),
                   max(tree[index*2][1], tree[index*2+1][1]))


def queryInSegmentTree(index, range, start, end):
    if range[0] <= start and end <= range[1]:
        return tree[index]

    mins, maxs = [], []

    mid = (start + end)//2
    if not (mid < range[0] or range[1] < start):
        tmpMin, tmpMax = queryInSegmentTree(index*2, range, start, mid)
        mins.append(tmpMin)
        maxs.append(tmpMax)

    if not (end < range[0] or range[1] < mid+1):
        tmpMin, tmpMax = queryInSegmentTree(index*2+1, range, mid+1, end)
        mins.append(tmpMin)
        maxs.append(tmpMax)

    return (min(mins), max(maxs))


if __name__ == '__main__':
    N, M = map(int, input().split())
    nums = [-1] + [int(input()) for _ in range(N)]

    tree = [(-1, -1)]*(4*N)
    initializeSegmentTree(1, 1, N)

    for _ in range(M):
        a, b = map(int, input().split())
        print(*queryInSegmentTree(1, (a, b), 1, N))
