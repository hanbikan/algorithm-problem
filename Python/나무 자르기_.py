import sys, collections
input = sys.stdin.readline

# f(x) = ax + b
class LinearFunction:
    def __init__(self, a, b, start_x):
        self.a = a
        self.b = b
        self.start_x = start_x

    def __str__(self):
        return f"[{self.a}x + {self.b} starting from {self.start_x}]"

    def get_intersection_x(self, other):
        return (other.b - self.b) / (self.a - other.a)

n = int(input())
a = list(map(int, input().split())) # height, 증가하는 수열
b = list(map(int, input().split())) # cost, 감소하는 수열

# dp[i] = min(dp[j] + a[i]*b[j]) (0 <= j < i) = f(x) = B*x + D (x = a[i], B = b[j], D = dp[j])
dp = [0] * n
stack = collections.deque()
for i in range(1, n):
    cur_f = LinearFunction(b[i - 1], dp[i - 1], 0)
    # stack에서 불필요한 함수 제거(cur_f가 높은(?) 함수들 제거)
    while stack:
        top_f = stack[-1]
        intersection_x = cur_f.get_intersection_x(top_f)
        if intersection_x < top_f.start_x:
            stack.pop()
        else:
            cur_f.start_x = intersection_x
            break
    stack.append(cur_f)

    # 현재 나무 처리 가능한 최소 비용을 구하기 위해 적절한 함수 찾기
    # f1(x) = x(start_x = 0), f2(x) = 0.5x + 1(start_x = 2) 상태에서 x=1에 해당하는 함수는 f1임
    x = a[i]
    l, r = 0, len(stack) - 1
    while l <= r:
        m = (l + r) // 2
        if stack[m].start_x >= x:
            r = m - 1
        else:
            l = m + 1
    stack_index = l - 1

    dp[i] = stack[stack_index].a * x + stack[stack_index].b

print(dp[-1])