import sys
input = sys.stdin.readline
PLUS, MINUS = 1, 2
INF = 100001

def calculate(origin, op, h):
    if origin == INF: return h
    elif op == PLUS:
        if abs(origin) < h: return h
        else: return origin
    else:
        if abs(origin) > abs(h): return h
        else: return origin

def update(index, start, end, op, left, right, h):
    propagate(index, start, end)
    
    # Out of range
    if right < start or end < left: return

    # In range
    if left <= start and end <= right:
        calculated = calculate(seg_tree[index], op, h)
        seg_tree[index] = calculated if op == PLUS else -calculated

        if start != end:
            calculated = calculate(lazy[index*2], op, h)
            print("!", seg_tree[index*2], calculated)
            lazy[index*2] = calculated if seg_tree[index*2] < calculated else -calculated
            calculated = calculate(lazy[index*2+1], op, h)
            lazy[index*2+1] = calculated if seg_tree[index*2+1] < calculated else -calculated
    else:
        mid = (start + end)//2
        update(index*2, start, mid, op, left, right, h)
        update(index*2+1, mid+1, end, op, left, right, h)
        seg_tree[index] = calculate(seg_tree[index], op, h)
        
def propagate(index, start, end):
    if lazy[index] != INF:
        op, h = PLUS if lazy[index] >= 0 else MINUS, abs(lazy[index])
        calculated = calculate(seg_tree[index], op, h)
        seg_tree[index] = calculated if op == PLUS else -calculated
        lazy[index] = INF

        if start != end:
            calculated = calculate(lazy[index*2], op, h)
            lazy[index*2] = calculated if seg_tree[index*2] < calculated else -calculated
            calculated = calculate(lazy[index*2+1], op, h)
            lazy[index*2+1] = calculated if seg_tree[index*2+1] < calculated else -calculated


def query(index, start, end, left, right):
    propagate(index, start, end)

    # Out of range
    if right < start or end < left: return -float('inf')

    # In range
    if left <= start and end <= right:
        return seg_tree[index]
    else:
        mid = (start + end)//2
        res1 = query(index*2, start, mid, left, right)
        res2 = query(index*2+1, mid+1, end, left, right)
        return max(res1, res2)


N, K = map(int,input().split())

seg_tree = [0]*(4*N)
lazy = [INF]*(4*N)

for _ in range(K):
    op, l, r, h = map(int,input().split())
    update(1, 1, N, op, l+1, r+1, h)

    print("@@@")
    for i in range(N):
        print(abs(query(1, 1, N, i+1, i+1)))