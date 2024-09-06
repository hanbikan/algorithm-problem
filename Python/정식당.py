import sys

input = sys.stdin.readline

# 일반
# 특별: 2만 원 이상 주문 시
# 서비스: 일반 + 특별 5만 원 이상일 시 최대 1개

A, B, C = map(int, input().split())
menus = {}  # 'noodle': ['A', 10000]
for _ in range(A):
    n, p = map(str, input().split())
    menus[n] = ['A', int(p)]

for _ in range(B):
    n, p = map(str, input().rstrip().split())
    menus[n] = ['B', int(p)]

for _ in range(C):
    n = str(input().rstrip())
    menus[n] = ['C', 0]

N = int(input())
ap = 0
bp = 0
bc = 0
cc = 0
for _ in range(N):
    n = str(input().rstrip())
    if menus[n][0] == 'A':
        ap += menus[n][1]
    elif menus[n][0] == 'B':
        bp += menus[n][1]
        bc += 1
    else:
        cc += 1

if cc >= 2:
    print("No")
elif cc == 1:
    if ap + bp >= 50000:
        if bc >= 1 and ap >= 20000:
            print("Okay")
        elif bc == 0:
            print("Okay")
        else:
            print("No")
    else:
        print("No")
else:
    if bc >= 1 and ap >= 20000:
        print("Okay")
    elif bc == 0:
        print("Okay")
    else:
        print("No")