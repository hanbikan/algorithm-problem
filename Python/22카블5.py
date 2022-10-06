import sys
input = sys.stdin.readline

def update(v1, v2):
    global cells
    for i in range(1, 50):
        for j in range(1, 50):
            if cells[i][j] == v1:
                cells[i][j] = v2

def find(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def merge(x, y):
    x1, y1 = convert_to_position(x)
    px = find(x)
    px1, py1 = convert_to_position(px)
    tmp = cells[px1][py1]

    py = find(y)
    for i in range(1, 51):
        for j in range(1, 51):
            cur_pos = convert_to_single(i, j)
            if find(cur_pos) == py:
                union(x, cur_pos)
                cells[i][j] = "EMPTY"
    
    cells[px1][py1] = tmp

#
def union(x, y):
    px, py = find(x), find(y)
    parents[py] = px

#
def convert_to_single(x, y):
    x -= 1
    y -= 1
    return x*50 + y

#
def convert_to_position(single):
    return [single // 50 + 1, single % 50 + 1]

#
def unmerge(x, y):
    pos = convert_to_single(x, y)
    parent = find(pos)

    to_unmerge = []
    for i in range(1, 51):
        for j in range(1, 51):
            cur_pos = convert_to_single(i, j)
            if find(cur_pos) == parent:
                to_unmerge.append(cur_pos)
    
    px, py = convert_to_position(parent)
    tmp = cells[px][py]
    for cur_pos in to_unmerge:
        parents[cur_pos] = cur_pos

        cur_x, cur_y = convert_to_position(cur_pos)
        cells[cur_x][cur_y] = "EMPTY"
    cells[x][y] = tmp


def solution(commands):
    answer = []

    global cells, parents
    cells = [["EMPTY"]*51 for _ in range(51)]
    parents = [i for i in range(50*50)]
    for command in commands:
        words = command.split()

        if words[0] == "UPDATE":
            if len(words) == 4:
                x, y = int(words[1]), int(words[2])
                px, py = convert_to_position(find(convert_to_single(x, y)))
                cells[px][py] = words[3]
            else:
                update(words[1], words[2])
        elif words[0] == "MERGE":
            pos1 = convert_to_single(int(words[1]), int(words[2]))
            pos2 = convert_to_single(int(words[3]), int(words[4]))
            px1, py1 = convert_to_position(find(pos1))
            if cells[px1][py1] == "EMPTY":
                merge(pos2, pos1)
            else:
                merge(pos1, pos2)
        elif words[0] == "UNMERGE":
            unmerge(int(words[1]), int(words[2]))
        else:
            x, y = int(words[1]), int(words[2])
            px, py = convert_to_position(find(convert_to_single(x, y)))
            answer.append(cells[px][py])

    return answer

#print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))
#print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "PRINT 1 1", "PRINT 1 2", "MERGE 2 2 2 1", "PRINT 2 1", "PRINT 2 2", "MERGE 2 1 1 1", "PRINT 1 1","PRINT 1 2","PRINT 2 1","PRINT 2 2", "UNMERGE 2 2", "PRINT 1 1","PRINT 1 2","PRINT 2 1","PRINT 2 2"]))