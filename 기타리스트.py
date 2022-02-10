import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, S, M = map(int, input().split())
    V = list(map(int, input().split()))
    
    res = -1

    prev = set([S])
    for i in range(N):
        nxt = set()

        for p in prev:
            if(0 <= p + V[i] <= M):
                nxt.add(p+V[i])
            if(0 <= p - V[i] <= M):
                nxt.add(p-V[i])

        if len(nxt) == 0:
            break

        prev = nxt
    else:              
        res = max(prev)

    print(res)