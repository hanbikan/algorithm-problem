import sys
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))

    # Set sums
    a_sums = {}
    for i in range(n):
        cur_sum = 0
        for j in range(i, n):
            cur_sum += A[j]

            if a_sums.get(cur_sum):
                a_sums[cur_sum] += 1
            else:
                a_sums[cur_sum] = 1

    b_sums = {}
    for i in range(m):
        cur_sum = 0
        for j in range(i, m):
            cur_sum += B[j]

            if b_sums.get(cur_sum):
                b_sums[cur_sum] += 1
            else:
                b_sums[cur_sum] = 1

    # Solution
    count = 0
    for k, v in a_sums.items():
        if b_sums.get(T-k):
            count += v*b_sums[T-k]

    print(count)
