import sys, collections

S, X, Y = 0, 1, 2


def get_intersection_x(l1, l2):
  return (l2[Y] - l1[Y]) / (l1[X] - l2[X])


input = sys.stdin.readline
n = int(input())
a, b, c = map(int, input().split())
nums = list(map(int, input().split()))

cur = 0

# dp[i] = max(dp[j] + f(p[i] - p[j])) (0 <= j < i) = max(-2ap[j]p[i] + ap[j]^2 - bp[j] + dp[j]) + ap[i]^2 + bp[i] + c
# f(x) = -2ap[j]x + ap[j]^2 - bp[j] + dp[j] (x = p[i])
# convex hull: -2ap[j] 기울기 단조감소
dp = 0
stack = collections.deque([[0.0, 0.0, 0.0]])
p = 0
for num in nums:
  p += num
  x = p

  # x가 이미 넘어간 앞에 있는 직선 제거(p[i]는 단조증가 하기 때문에 bisect 불필요)
  while len(stack) >= 2 and stack[1][S] <= x:
    stack.popleft()

  dp = (stack[0][X] * x + stack[0][Y]) + a * p**2 + b * p + c

  # 직선 추가 이전에 불필요한 직선 뒤에서부터 제거
  cur_f = [0, -2.0 * a * p, a * p**2 - b * p + dp]
  while stack:
    top = stack[-1]
    intersection_x = get_intersection_x(cur_f, top)
    if intersection_x < top[S]:
      stack.pop()
    else:
      cur_f[S] = intersection_x
      break

  # 직선 추가
  stack.append(cur_f)

print(round(dp))
