def solution(List):
    for i in range(0, len(List)-2):
        if IsSubListsBitonic(List, i): return len(List)-i
    return False

def IsSubListsBitonic(List, n):
    prev=getSubLists(List)
    for i in range(n-1):
        cur=[]
        for j in range(len(prev)):
            cur+=getSubLists(prev[j])
        prev=cur
    for i in range(len(prev)):
        if IsBitonic(prev[i]): return True
    return False

def getSubLists(List):
    RET = []
    for i in range(len(List)):
        RET.append(List[:i]+List[i+1:])
    return RET

def IsBitonic(nums):
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            for j in range(i+1, len(nums)-1):
                if nums[j]<nums[j+1]: return False
            return True
    return True

N = int(input())
lst = str(input())
lst = lst.split()
for i in range(len(lst)):
    lst[i]=int(lst[i])
print(solution(lst))