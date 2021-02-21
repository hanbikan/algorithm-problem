N=4
W = [[0,12,15,20],[5,0,9,10],[6,13,0,12],[8,8,9,0]]
def TSP(visited, cur): #0000 0
    if visited == (1<<N)-1:
        if W[cur][0]: return W[cur][0]
        else: return False
    
    ret=False
    for i in range(N):
        if visited&(1<<i): continue
        if W[cur][i]==0: continue
        ret = min(ret, TSP(i, visited | (1<<i)) + W[cur][i])
    return ret


print(TSP(1, 0))