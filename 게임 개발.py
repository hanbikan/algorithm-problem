import sys

input = sys.stdin.readline

N = int(input())
buildTimes = [-1 for _ in range(N+1)]
prevBuild = {i: [] for i in range(N+1)}
realBuildTimes = [-1 for _ in range(N+1)]


def getBuildTime(index):
    global realBuildTimes
    RET = buildTimes[index]
    for cur in prevBuild[index]:
        if realBuildTimes[cur] != -1:
            RET = max(RET, buildTimes[index]+realBuildTimes[cur])
        else:
            RET = max(RET, buildTimes[index]+getBuildTime(cur))
    realBuildTimes[index] = RET
    return RET


for i in range(N):
    curNums = list(map(int, input().split()))
    buildTimes[i+1] = curNums[0]
    for j in range(1, len(curNums)-1):
        prevBuild[i+1].append(curNums[j])

for i in range(1, N+1):
    print(getBuildTime(i))
