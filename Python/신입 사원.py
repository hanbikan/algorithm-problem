T = int(input())
for _ in range(T):
    N = int(input())
    scores = [0]*(N+1)
    for _ in range(N):
        curDoc, curInt = map(int, input().split())
        scores[curDoc] = curInt
    
    minInt = scores[1]
    cntDropout = 0
    for i in range(2, N+1):
        if scores[i] > minInt:
            cntDropout += 1
        else:
            minInt = scores[i]
    print(N-cntDropout)