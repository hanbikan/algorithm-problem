import sys
input = sys.stdin.readline
INF = 1000000000


def bellmanFord():
    global isAvailable

    for i in range(1, n+1):
        for j in range(1, n+1):
            for target, wasted in info[j]:
                if dp[target] > wasted + dp[j]:
                    dp[target] = wasted + dp[j]

                    if i == n:
                        isAvailable = True


if __name__ == '__main__':
    # 입력
    tc = int(input())

    for _ in range(tc):
        n, m, w = map(int, input().split())

        info = [[] for _ in range(n+1)]

        # 도로
        for _ in range(m):
            s, e, t = map(int, input().split())

            info[s].append((e, t))
            info[e].append((s, t))

        # 웜홀
        for _ in range(w):
            s, e, t = map(int, input().split())

            info[s].append((e, -t))

        # 탐색
        isAvailable = False
        dp = [INF]*(n+1)
        bellmanFord()

        # 출력
        if isAvailable:
            print("YES")
        else:
            print("NO")
