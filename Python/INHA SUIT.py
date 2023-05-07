from queue import PriorityQueue
import sys
input = sys.stdin.readline
T_INDEX, W_INDEX, H_INDEX = 0, 1, 2

def solution():
    queue = PriorityQueue()
    queue.put([0, 0, 1]) # t, w, h: used T for t times and located at (w, h)
    dp = [[float('inf')] * 21 for _ in range(N + 1)] # dp[w][h] = t

    while (not queue.empty()):
        t, w, h = queue.get()
        for hole in holes[w]:
            next_t = t if is_available_using_OABC(h, hole) else t + 1
            if (next_t <= T and dp[w + 1][hole] > next_t):
                dp[w + 1][hole] = next_t
                if w + 1 < N: queue.put([next_t, w + 1, hole])
    
    result = min(dp[-1])
    if result == float('inf'): return -1
    else: return result

def is_available_using_OABC(current_height, hole):
    return (current_height == hole) or (current_height + 1 == hole) or min(20, current_height * 2) == hole or (current_height - 1 == hole)

# O
# A: += 1
# B: *= 2(max 20)
# C: -= 1
# T: = move to anywhere

N = int(input())
T = int(input())
holes = []
for _ in range(N):
    holes.append(list(map(int, input().split()))[1:])

print(solution())