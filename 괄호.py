T = int(input())
liststr = []
for i in range(T):
    tmp = input()
    liststr.append(tmp)
for s in liststr:
    flag = True
    curStatus = 0
    for i in range(len(s)):
        if s[i] == '(': curStatus+=1
        elif s[i] == ')': curStatus-=1
        if curStatus < 0:
            flag = False
            break
    if curStatus != 0: flag = False
    if flag: print('YES')
    else: print('NO')