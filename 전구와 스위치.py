import sys
import copy
input = sys.stdin.readline


def switch(index, map):
    for i in range(index-1, index+2):
        if 0 <= i <= N-1:
            map[i] = not map[i]

    return map


def getSwitchCount(map, count):
    switchCount = count
    newMap = copy.deepcopy(map)

    for i in range(1, N):
        if newMap[i-1] == True:
            newMap = switch(i, newMap)
            switchCount += 1

    # 모두 False인지 확인
    for i in range(N):
        if newMap[i] == True:
            return -1

    return switchCount


N = int(input())

input1 = input().rstrip()
input2 = input().rstrip()
# True -> False로 바꿔야함
map = [input1[i] != input2[i] for i in range(N)]

switchCountWithoutSwitchingZero = getSwitchCount(map, 0)
if switchCountWithoutSwitchingZero != -1:
    print(switchCountWithoutSwitchingZero)
else:
    print(getSwitchCount(switch(0, map), 1))
