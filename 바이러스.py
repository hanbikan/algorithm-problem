import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000) 
class Computer:
    def __init__(self, val):
        self.val = val
        self.adjacent = []

RET=0
C = int(read())
Computers = [Computer(i) for i in range(C)]
listInfected = [False for i in range(C)]
listInfected[0] = True
N = int(read())
for i in range(N):
    a, b = map(int, read().strip().split())
    Computers[a-1].adjacent.append(b-1)
    Computers[b-1].adjacent.append(a-1)

todo = [0]
while todo != []:
    nexttodo = []
    for i in range(len(todo)):
        for j in range(len(Computers[todo[i]].adjacent)):
            if not listInfected[Computers[todo[i]].adjacent[j]]:
                listInfected[Computers[todo[i]].adjacent[j]] = True
                nexttodo.append(Computers[todo[i]].adjacent[j])
                RET+=1
    todo = nexttodo

print(RET)