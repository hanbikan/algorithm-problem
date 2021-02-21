def solution(roadmap):
    DP = [[0 for i in range(len(roadmap[0]))] for j in range(len(roadmap))]
    DP[0][0]=1
def getPossiblePosition(roadmap, curX, curY):
    RET = []
    curH = roadmap[curX][curY]
    if curX-1>=0 and roadmap[curX-1][curY]<curH: RET.append([curX-1, curY])
    if curY-1>=0 and roadmap[curX][curY-1]<curH: RET.append([curX, curY-1])
    if curX+1<=len(roadmap)-1 and roadmap[curX+1][curY]<curH: RET.append([curX+1, curY])
    if curY+1<=len(roadmap[0])-1 and roadmap[curX][curY+1]<curH: RET.append([curX, curY+1])
    return RET

def printDP(DP):
    for i in range(len(DP)):
        print(DP[i])
    print()
"""
tmp = input()
tmp=tmp.split()
N, M = int(tmp[0]), int(tmp[1])
roadmap=[]
for i in range(N):
    tmp = input()
    tmp=tmp.split()
    for j in range(M):
        tmp[j]=int(tmp[j])
    roadmap.append(tmp)
"""
roadmap=[[50,45,37,32,30],[35,50,40,20,25],[30,30,25,17,28],[27,24,22,15,10]]
solution(roadmap)