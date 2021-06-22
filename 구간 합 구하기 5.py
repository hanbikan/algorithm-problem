import sys
input = sys.stdin.readline

if __name__ == '__main__':
    # 입력
    N, M = map(int, input().split())
    nums = [[0]*(N+1)] + [[0]+list(map(int, input().split()))
                          for _ in range(N)]

    # 누적합
    for i in range(1, N+1):
        for j in range(1, N+1):
            nums[i][j] += nums[i][j-1] + nums[i-1][j] - nums[i-1][j-1]

    # 출력
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())

        print(nums[x2][y2] - nums[x1-1][y2] -
              nums[x2][y1-1] + nums[x1-1][y1-1])
