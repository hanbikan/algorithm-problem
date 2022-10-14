from collections import defaultdict, deque
import sys
input = sys.stdin.readline
 
def f():
    a_items = sorted(a.items())
    b_items = sorted(b.items(), reverse=True)
    i, j = 0, 0
    while i < len(a_items) and j < len(b_items):
        ak, av = a_items[i]
        bk, bv = b_items[i]

        if ak < bk: return True
        elif ak > bk: return False

        minn = min(av, bv)
        a_items[i][1] -= minn
        b_items[i][1] -= minn
        
        if a_items[i][1] == 0:
            i += 1
            if i >= len(a_items): return False
        if b_items[i][1] == 0:
            j += 1
            if j >= len(b_items): return True


t = int(input())
for _ in range(t):
    q = int(input())
    a, b = defaultdict(int), defaultdict(int)
    a['a'] = 1
    b['a'] = 1
    for _ in range(q):
        d, k, x = map(str, input().rstrip().split())
        d, k = int(d), int(k)
        if d == 1:
            for i in range(len(x)):
                a[x[i]] += k
        else:
            for i in range(len(x)):
                b[x[i]] += k
    
        if (f()): print("YES")
        else: print("NO")