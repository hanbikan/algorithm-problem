import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    costs = [0]*(N+1)

    for i in range(1, N+1):
        cur_input = list(map(int, input().split()))

        prev_max_time = 0
        for j in range(2, 2 + cur_input[1]):
            prev_max_time = max(prev_max_time, costs[cur_input[j]])

        costs[i] = prev_max_time + cur_input[0]

    print(max(costs))
