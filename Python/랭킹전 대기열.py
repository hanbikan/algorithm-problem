import sys
input = sys.stdin.readline

p, m = map(int,input().split())
rooms = [] # rooms[i] = [[10, "a"], [15, "b"]]
for _ in range(p):
    level, id = map(str,input().rstrip().split())
    level = int(level)
    flag = False
    for i in range(len(rooms)):
        if len(rooms[i]) == 0 or (abs(rooms[i][0][0] - level) <= 10 and len(rooms[i]) < m):
            rooms[i].append([level, id])
            flag = True
            break
    if not flag:
        rooms.append([[level, id]])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    room.sort(key = lambda x: x[1])
    for level, id in room:
        print(level, id)
