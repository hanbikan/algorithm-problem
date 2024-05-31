import sys, math

input = sys.stdin.readline

W, H = map(float, input().split())

d = math.sqrt(W**2 + H**2)
a = H * W / (W + d)
b = H * d / (W + d)

w = 0.5 * math.sqrt(W**2 + a**2)
h = (W * (H - a)) / (2 * w)

print(round(w, 2), round(h, 2))