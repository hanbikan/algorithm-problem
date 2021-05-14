import sys
input = sys.stdin.readline


class Node:
    def __init__(self):
        self.start = None
        self.end = None
        self.left = None
        self.right = None
        self.var = None


def initializeSegmentTree(node, start, end):
    node.start = start
    node.end = end

    if start == end:  # 말단
        node.var = nums[start]
    else:
        # 자식 노드 생성하고 dfs 로직으로 초기화
        node.left = Node()
        initializeSegmentTree(node.left, start, (start+end)//2)

        node.right = Node()
        initializeSegmentTree(node.right, (start+end)//2+1, end)

        # 자식을 합함
        node.var = node.left.var + node.right.var


def modifySegmentTree(node):
    node.var += c-nums[b]  # 세그먼트 트리 값 변경

    if node.start == node.end:
        nums[b] = c  # nums도 꼭 수정을 해야함
        return

    # b가 해당 자식의 범위에 있을 시 탐색
    if node.left and node.left.start <= b <= node.left.end:
        modifySegmentTree(node.left)
    elif node.right and node.right.start <= b <= node.right.end:
        modifySegmentTree(node.right)


def setSegmentSum(node, start, end):
    global sum

    if start <= node.start and node.end <= end:
        # sum 갱신
        sum += node.var

        # 나뉘어진 새 범위에 대해서 탐색
        if not (node.start == start and node.end == end):
            if b <= node.start-1 and node.left and start <= node.left.end:
                setSegmentSum(node.left, start, node.start-1)
            if node.end+1 <= c and node.right and node.right.start <= end:
                setSegmentSum(node.right, node.end+1, end)

    else:
        if node.left and start <= node.left.end:
            setSegmentSum(node.left, start, end)
        if node.right and node.right.start <= end:
            setSegmentSum(node.right, start, end)


N, M, K = map(int, input().split())
nums = [0]
for _ in range(N):
    nums.append(int(input()))

root = Node()
initializeSegmentTree(root, 1, N)

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:
        modifySegmentTree(root)
    elif a == 2:
        sum = 0
        setSegmentSum(root, b, c)
        print(sum)
