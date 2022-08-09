import sys
read = sys.stdin.readline
N = int(read())
conferences = []
START, END = 0, 1

for i in range(N):
    conferences.append(list(map(int, read().strip().split())))
conferences = sorted(conferences, key=lambda x: x[0])
conferences = sorted(conferences, key=lambda x: x[1])

lastEnd = 0
RET=0
for s, e in conferences:
    if s >= lastEnd:
        lastEnd = e
        RET+=1
print(RET)