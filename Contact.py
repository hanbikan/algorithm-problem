import re
N = int(input())
for _ in range(N):
    cur = input()
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(cur)
    if m: print('YES')
    else: print('NO')