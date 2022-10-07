import sys
input = sys.stdin.readline
X, Y = 0, 1

def is_line():
    dp = [[1,3], [2,3], [0,2], [0,1]]
    dq = [[0,2], [0,1], [1,3], [2,3]]
    dl = [X,Y,X,Y]
    for i in range(4):
        p, q, l = dp[i], dq[i], dl[i]
        nl = (l + 1) % 2
        if not P[p[0]][nl] == Q[q[0]][nl]: continue
        for j in range(2):
            if P[p[0]][l] <= Q[q[j]][l] <= P[p[1]][l] or Q[q[0]][l] <= P[p[j]][l] <= Q[q[1]][l]:
                return True
    return False

def is_point():
    return P[0] == Q[3] or P[1] == Q[2] or P[2] == Q[1] or P[3] == Q[0]

x1, y1, x2, y2 = map(int,input().split()) # P
P = [[x1,y1], [x1,y2], [x2,y1], [x2,y2]]
x3, y3, x4, y4 = map(int,input().split()) # Q
Q = [[x3,y3], [x3,y4], [x4,y3], [x4,y4]]

if P[3][X] < Q[0][X] or Q[3][X] < P[0][X] or P[3][Y] < Q[0][Y] or Q[3][Y] < P[0][Y]:
    print("NULL")
elif is_point():
    print("POINT")
elif is_line():
    print("LINE")
else:
    print("FACE")
