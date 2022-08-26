import sys
input = sys.stdin.readline

def find_min():
    for i in range(10001):
        if counts[i] > 0:
            return i
    return -1

N = int(input())
nums = list(map(int,input().split()))

counts = [0]*10001
for n in nums:
    counts[n] += 1

cur_sum = sum(nums)
acc_nums = []
for n in nums:
    acc_nums.append(cur_sum)
    cur_sum -= n

maxx = 0
max_index = -1
to_print = []
cur_min = min(nums)
for i in range(1, N-2 + 1):
    prev_num = nums[i-1]
    counts[prev_num] -= 1
    if counts[prev_num] == 0 and cur_min == prev_num:
        cur_min = find_min()

    score = (acc_nums[i] - cur_min) / (N - i - 1)
    if score > maxx:
        maxx = score
        max_index = i
        to_print = [i]
    elif score == maxx:
        to_print.append(i)

for n in to_print:
    print(n)

