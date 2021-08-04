import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def bs(n):
    left, right = 0, len(stack)-1

    while left <= right:
        mid = (left+right)//2

        if nums[stack[mid]] < n:
            left = mid + 1
        else:
            right = mid - 1

    return left


def dfs():
    global currentNode, currentLength

    if currentLength == stackLength:
        return True

    nexts = tree.get(currentNode)
    if nexts:
        for next in nexts:
            currentNode = next
            currentLength += 1
            if dfs():
                stack.append(nums[next])
                return True
            currentLength -= 1

    return False


if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))

    stack = []
    tree = {}

    for i in range(N):
        # 기본 LIS
        n = nums[i]
        minBiggerIndex = bs(n)

        if minBiggerIndex == len(stack):
            stack.append(i)
        else:
            if nums[stack[minBiggerIndex]] == n:
                continue

            stack[minBiggerIndex] = i

        # 트리
        if minBiggerIndex == 0:
            if tree.get('R'):
                tree['R'].add(i)
            else:
                tree['R'] = set([i])

            continue

        prevIndex = stack[minBiggerIndex-1]
        if nums[prevIndex] < n:
            if tree.get(prevIndex):
                tree[prevIndex].add(i)
            else:
                tree[prevIndex] = set([i])

            continue

    stackLength = len(stack)
    print(stackLength)

    currentNode = 'R'
    currentLength = 0
    stack = []
    dfs()
    print(*reversed(stack))
