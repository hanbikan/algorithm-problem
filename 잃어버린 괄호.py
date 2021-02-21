def IsDigit(c):
    if c>='0' and c<='9': return True
    return False

STR = input()
parsed = []
startIdx = -1 # -1이면 지정하기 전 상태
for i in range(len(STR)):
    if IsDigit(STR[i]):
        if(startIdx==-1): startIdx=i
    else:
        parsed.append(int(STR[startIdx:i]))
        parsed.append(STR[i])
        startIdx = -1
parsed.append(int(STR[startIdx:len(STR)]))

RET = parsed[0]
IsReachedMinus = False
for i in range(1, len(parsed), 2):
    if IsReachedMinus:
        RET-=parsed[i+1]
    else:
        if parsed[i]=='+':
            RET+=parsed[i+1]
        elif parsed[i]=='-':
            RET-=parsed[i+1]
            IsReachedMinus = True
print(RET)