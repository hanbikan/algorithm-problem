import sys
input = sys.stdin.readline

'''
222 221 212 211  122 121 112 111 
223 224 213 214  123 124 113 114
232 231 242 241  132 131 142 141
233 234 243 244  133 134 143 144

322 321 312 311  422 421 412 411
323 324 313 314  423 424 413 414
332 331 342 341  432 431 442 441
333 334 343 344  433 434 443 444
'''

# xxx1 -> 1
# xx1x -> 2
# x1xx -> 4
# 1xxx -> 8
# 3221 moves 10 times to right
# 10 = 8 + 2
# 4211

# Column: 1 -> 4, 2 -> 3
# dir: 0 = ⬇, 1 = ⬆
c1 = ['1', '4', '1']
c2 = ['2', '3', '2']
def move_in_column(strr, digit, dir):
    if digit < 0 or digit > d - 1:
        return False

    if strr[digit] == c1[dir]:
        strr[digit] = c1[dir + 1]
    elif strr[digit] == c2[dir]:
        strr[digit] = c2[dir + 1]
    elif strr[digit] == c1[dir + 1]:
        strr[digit] = c1[dir]
        strr = move_in_column(strr, digit - 1, dir)
    else: # c2[dir + 1]
        strr[digit] = c2[dir]
        strr = move_in_column(strr, digit - 1, dir)
    
    return strr

# Row: 2 -> 1, 3 -> 4
# dir: 0 = ->, 1 = <-
r1 = ['2', '1', '2']
r2 = ['3', '4', '3']
def move_in_row(strr, digit, dir):
    if digit < 0 or digit > d - 1:
        return False

    if strr[digit] == r1[dir]:
        strr[digit] = r1[dir + 1]
    elif strr[digit] == r2[dir]:
        strr[digit] = r2[dir + 1]
    elif strr[digit] == r1[dir + 1]:
        strr[digit] = r1[dir]
        strr = move_in_row(strr, digit - 1, dir)
    else: # r2[dir + 1]
        strr[digit] = r2[dir]
        strr = move_in_row(strr, digit - 1, dir)
    
    return strr

# 49 -> 0
# mod: 2^n, index: d - 1 - n
def f(d, n, x, y):
    row_dir = 0 if x > 0 else 1
    cur_n = 49
    cur_x = abs(x)
    while cur_x > 0:
        if cur_x // (2 ** cur_n) >= 1:
            n = move_in_row(n, d - 1 - cur_n, row_dir)
            cur_x %= 2 ** cur_n
            if not n:
                return False
        cur_n -= 1
    
    column_dir = 0 if y > 0 else 1
    cur_n = 49
    cur_y = abs(y)
    while cur_y > 0:
        if cur_y // (2 ** cur_n) >= 1:
            n = move_in_column(n, d - 1 - cur_n, column_dir)
            cur_y %= 2 ** cur_n
            if not n:
                return False
        cur_n -= 1

    return n

d, n = map(int,input().split())
n = list(str(n))
x, y = map(int,input().split())

res = f(d, n, x, -y)
if res:
    print("".join(res))
else:
    print(-1)