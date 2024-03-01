from bisect import bisect_left
import sys
input = sys.stdin.readline

def set_result(summ):
    global result
    if result == None:
        result = summ
        return
    
    cur_abs, prev_abs = abs(k - summ), abs(k - result)
    if cur_abs < prev_abs or (cur_abs == prev_abs and summ < result):
        result = summ

T = int(input())
for _ in range(T):
    k, n = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(4)]

    if (n == 1):
        print(sum(nums[i][0] for i in range(4)))
        continue

    two_sums = []
    for line_index in range(0, 4, 2):
        sums = []
        for i in range(n):
            for j in range(n):
                summ = nums[line_index][i] + nums[line_index + 1][j]
                sums.append(summ)
        sums.sort()
        two_sums.append(sums)
    
    result = None
    for sum1 in two_sums[0]:
        sum2 = k - sum1
        index = bisect_left(two_sums[1], sum2)

        if 0 <= index < len(two_sums[1]):
            set_result(sum1 + two_sums[1][index])
        if 0 <= index - 1 < len(two_sums[1]):
            set_result(sum1 + two_sums[1][index - 1])
    print(result)