import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline


def search(node):
    stack.append(node)
    visitInfo[node] = curSearchStart

    next = nums[node]
    nextVisitInfo = visitInfo[next]

    # 이번 탐색 때 방문한 경우
    if nextVisitInfo == curSearchStart:
        global notInCycle
        notInCycle -= len(stack) - stack.index(next)

    # 방문한 적이 없을 경우
    elif nextVisitInfo == 0:
        search(next)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        # 입력
        N = int(input())
        nums = [-1] + list(map(int, input().split()))

        # 탐색
        notInCycle = N
        visitInfo = [0]*(N+1)

        for i in range(1, N+1):
            # 방문한 적이 없을 경우
            if visitInfo[i] == 0:
                curSearchStart = i
                stack = []

                search(i)

        # 출력
        print(notInCycle)
