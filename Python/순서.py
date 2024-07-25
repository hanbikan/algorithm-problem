import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    cur = []
    for i in range(N):
        num = nums[i]
        to_append = num + 1
        for j in range(len(cur)):
            if cur[j] >= to_append:
                cur[j] += 1
        cur.append(to_append)

    # check
    flag = True
    for i in range(N):
        if not 1 <= cur[i] <= N:
            flag = False
            break

    if flag:
        print(*cur)
    else:
        print("IMPOSSIBLE")
