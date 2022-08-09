def IsGroupWord(word):
    RET = True
    curDict = [0] * 26
    for i in range(len(word)):
        idx = ord(word[i])-ord('a')
        if curDict[idx]>0 and i-1>=0 and cur[i-1]!=word[i]:
            RET=False
            break
        curDict[idx]+=1
    return RET

RET = 0
N = int(input())
for i in range(N):
    cur = input()
    if IsGroupWord(cur): RET += 1

print(RET)