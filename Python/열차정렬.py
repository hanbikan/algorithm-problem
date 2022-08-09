import sys
import bisect
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    weights = []
    indices = {}
    for i in range(N):
        cur = int(input())
        weights.append(cur)
        indices[cur] = i

    # LIS
    dp = [0]*N
    stack = []
    lis_length = 0
    for i in range(N):
        index = bisect.bisect_left(stack, weights[i])

        if index >= lis_length:
            stack.append(weights[i])
            lis_length += 1
        else:
            stack[index] = weights[i]

        dp[i] = index

    cur_length = lis_length
    lis = []
    for i in range(N-1, -1, -1):
        if dp[i] == cur_length-1:
            lis.append(weights[i])
            cur_length -= 1

    # LDS
    dp = [0]*N
    stack = []
    lds_length = 0
    for i in range(N):
        index = bisect.bisect_left(stack, -weights[i])

        if index >= lds_length:
            stack.append(-weights[i])
            lds_length += 1
        else:
            stack[index] = -weights[i]

        dp[i] = index

    cur_length = lds_length
    lds = []
    for i in range(N-1, -1, -1):
        if dp[i] == cur_length-1:
            lds.append(weights[i])
            cur_length -= 1

    print(lis, lds)
    # LIS for indices
    toPrint = max(lis_length, lds_length)
    for i in range(lis_length):
        cur = lis[i]
        try:
            index = lds.index(cur)
            toPrint = max(i, index) + max(lis_length-i, lds_length-index)
            break
        except:
            continue

    print(toPrint)
