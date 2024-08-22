import sys, heapq, copy
input = sys.stdin.readline

def to_string(nums):
    return ''.join(map(str, nums))

def apply_control(nums, control):
    l, r, _ = control
    new_nums = copy.deepcopy(nums)
    new_nums[l] = nums[r]
    new_nums[r] = nums[l]
    return new_nums

def test(nums):
    for i in range(1, N):
        if nums[i - 1] > nums[i]:
            return False
    return True

def f():
    min_num = min(A)
    max_num = max(A)

    # dp[nums]: min cost
    dp = {}
    dp[to_string(A)] = 0

    # pq: [cost, nums]
    pq = [[0, A]]  # cost, nums
    while pq:
        cur_cost, cur_nums = heapq.heappop(pq)

        # test
        if cur_nums[0] == min_num and cur_nums[-1] == max_num and test(cur_nums):
            return cur_cost

        # try all the controls
        for control in controls:
            l, r, c = map(int, control)
            new_nums = apply_control(cur_nums, control)
            new_str = to_string(new_nums)
            new_cost = cur_cost + c

            if not dp.get(new_str) or (new_cost < dp[new_str]):
                dp[new_str] = new_cost
                heapq.heappush(pq, [new_cost, new_nums])

    return -1

N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    A[i] -= 1 # 0~9
M = int(input())
controls = []
for _ in range(M):
    l, r, c = map(int, input().split())
    l -= 1
    r -= 1
    controls.append([l, r, c])

print(f())