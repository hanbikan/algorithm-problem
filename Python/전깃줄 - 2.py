import sys
import bisect
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    info.sort()

    # LIS
    stack = []
    stack_length = 0
    dp = [0]*N

    for i in range(N):
        a, b = info[i]
        index = bisect.bisect_left(stack, b)

        if index >= stack_length:
            stack.append(b)
            stack_length += 1
        else:
            stack[index] = b

        dp[i] = index

    lis = set()
    for i in range(N-1, -1, -1):
        if dp[i] == stack_length-1:
            lis.add(info[i][0])
            stack_length -= 1

    # 출력
    lis_length = len(lis)
    print(N - lis_length)
    for i in range(N):
        a, _ = info[i]

        if a not in lis:
            print(a)
