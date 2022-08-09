import sys
input = sys.stdin.readline


def getMinTimeAndCaseCount(N, K):
    if N >= K:
        return N-K, 1

    curTime = 0
    todo = [N]
    minTimes = [float('inf')]*100001
    minTimes[N] = 0

    while todo:
        print(todo)
        nextTodo = []
        caseCount = 0
        curTime += 1

        for n in todo:
            if n > K:
                next = [n-1]
            elif n >= 2 and (K / n) % 2 == 0 and K != 0:
                next = [n*2]
            else:
                next = [n-1, n+1, n*2]

            for i in next:
                # 범위 벗어날 경우
                if i < 0 or i > 100000:
                    continue

                # 일치 시 카운트
                if i == K:
                    caseCount += 1

                # 시간 체크하여 방문
                if minTimes[i] >= curTime:
                    minTimes[i] = curTime
                    nextTodo.append(i)

        # 1번이라도 카운트 되었을 시
        if caseCount > 0:
            return curTime, caseCount

        todo = nextTodo


if __name__ == '__main__':
    N, K = map(int, input().split())

    minTime, caseCount = getMinTimeAndCaseCount(N, K)
    print(minTime)
    print(caseCount)
