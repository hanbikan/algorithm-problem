def solution(N, K, W, V):
    prev={}
    for i in range(len(W)):
        prev[W[i]] = V[i]

    for i in range(N-1):
        cur={}
        for item in prev.items():
            prevCurLength = len(cur)
            FlagDead = 0
            for j in range(len(W)):
                if item[0]+W[j]<=K:
                    if (cur.get(item[0]+W[j])!=None and cur[item[0]+W[j]]>item[1]+V[j]):
                        FlagDead = 1
                    cur[item[0]+W[j]] = item[1]+V[j]

            if prevCurLength==len(cur) and FlagDead==0:#Nothing Was Added
                cur[item[0]] = item[1]
        prev=cur
        print(cur)
    return max(cur.values())
 
def f(N,K,W,V): #N,K,W,V=7, 19, [9,8,1,6,2,3,7], [89,80,32,68,74,42,2]
    DP = [[0 for i in range(K+1)] for j in range(N+1)]
    
    for i in range(N):
        for j in range(1, K+1):
            DP[i][j]=DP[i-1][j]
            if j >= W[i]:
                DP[i][j] = max(DP[i][j], DP[i-1][j-W[i]] + V[i])
    print(DP)

'''
tmp = input()
tmp=tmp.split()
for i in range(2): tmp[i]=int(tmp[i])
N,K=tmp[0],tmp[1]

W,V=[],[]
for i in range(N):
    tmp = input()
    tmp=tmp.split()
    W.append(int(tmp[0]))
    V.append(int(tmp[1]))
'''
#N,K,W,V=7, 19, [9,8,1,6,2,3,7], [89,80,32,68,74,42,2]
N,K,W,V=4, 7, [6,4,3,5], [13,8,6,12]

f(N,K,W,V)