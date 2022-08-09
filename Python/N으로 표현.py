def solution(N, number): # 5 12
    answer = 0
    t=[[N]]
    for i in range(2):
        t=getNextListWithoutBracket(t, N)
        print(t)
        t=addBracketsToList(t)
        print(t)
        t=calculateAll(t)
        print(t)
        print()
    return answer

def getNextListWithoutBracket(lists, N):
    #prev = "5+5"
    RET = []
    for lst in lists:
        RET.append([lst[len(lst)-1]+N])
        RET.append([lst+"+"+str(N)])
        RET.append([lst+"-"+str(N)])
        RET.append([lst+"*"+str(N)])
        RET.append([lst+"/"+str(N)])
    return RET

def addBracketsToList(lists):
    addList = []
    for lst in lists:
        pmIndex = -1
        mdIndex = -1
        for i in range(len(lst)):
            if lst[i]=="+" or lst[i]=="-": pmIndex = i
            elif lst[i]=="*" or lst[i]=="/":
                mdIndex = i
                break
        if pmIndex != -1 and mdIndex != -1:
            bracketInt=calculateStr(lst[0:mdIndex])
            addList.append(bracketInt+lst[mdIndex:len(lst)])
    return lists+addList

def calculateAll(lists):
    i=0
    for lst in lists:
        lists[i] = calculateStr(lst)
        i+=1
    return lists

def calculateStr(st):
    RET = None
    op1, op2 = "", ""
    c = ""
    flag = 0
    for s in st:
        if s=="+" or s=="-" or s=="*" or s=="/":
            c = s
            flag = 1
        elif flag==0: op1+=s
        elif flag==1: op2+=s

    if c=="+": RET = int(op1)+int(op2)
    elif c=="-": RET = int(op1)-int(op2)
    elif c=="*": RET = int(op1)*int(op2)
    elif c=="/": RET = int(op1)//int(op2)
    if RET == None: return st
    return str(RET)

solution(5,12)