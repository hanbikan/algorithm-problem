import sys, math, functools, collections
input = sys.stdin.readline

def ccw(p1,p2,p3):
    return (p2[0]-p1[0])*(p3[1]-p2[1]) - (p2[1]-p1[1])*(p3[0]-p2[0])

def calculate_distance(p1,p2):
    return math.sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2))

def compare(p1,p2):
    c = ccw(base_point, p1, p2)
    if c == 0: # 직선에 있다면 더 가까운 것을 선택한다.
        return calculate_distance(base_point, p1) - calculate_distance(base_point, p2)
    return -c

N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

# convex hull
points.sort(key=lambda x: (x[1], x[0]))
base_point = points[0]
points.sort(key=functools.cmp_to_key(compare))

stack = collections.deque([points[0], points[1]])
for i in range(2, N):
    while len(stack) >= 2 and ccw(stack[-2], stack[-1], points[i]) <= 0:
        stack.pop()
    stack.append(points[i])

print(len(stack))