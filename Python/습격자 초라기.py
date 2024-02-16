import sys
input = sys.stdin.readline

def get_adjacent_indexes(index):
    left = index - 1 if (index - 1) % N != 0 else index + (N - 1)
    right = index + 1 if index % N != 0 else index - (N - 1)
    front = (index - 1 + N) % (2 * N) + 1
    sett = set([left, right, front])
    if index in sett:
        sett.remove(index)
    return list(sett)

def combine(index1, index2):
    enemies[index1] = float('inf')
    enemies[index2] = float('inf')
    adjs = get_adjacent_indexes(index1) + get_adjacent_indexes(index2)
    for adj in adjs:
        update_possible_counts(adj)

def update_possible_counts(index):
    possible_counts[index] = 0
    adjs = get_adjacent_indexes(index)
    for adj in adjs:
        if enemies[index] + enemies[adj] <= W:
            possible_counts[index] += 1

def get_possible_adjacent_indexes(index):
    res = []
    adjs = get_adjacent_indexes(index)
    for adj in adjs:
        if enemies[index] + enemies[adj] <= W:
            res.append(adj)
    return res

def f():
    global result
    
    entries = []
    for i in range(1, 2 * N + 1):
        if possible_counts[i] == 1:
            entries.append(i)

    while entries:
        i = entries.pop()
        if enemies[i] == float('inf'):
            continue

        if possible_counts[i] == 1:
            possible_adj = get_possible_adjacent_indexes(i)[0]
            combine(i, possible_adj)
            result += 1

            adjs = get_adjacent_indexes(possible_adj)
            for adj in adjs:
                if possible_counts[adj] == 1:
                    entries.append(adj)

T = int(input())
for _ in range(T):
    N, W = map(int,input().split())
    enemies = [list(map(int,input().split())) for _ in range(2)]
    enemies = [None] + enemies[0] + enemies[1]
    
    possible_counts = [0] * (2 * N + 1)
    for i in range(1, 2 * N + 1):
        update_possible_counts(i)
    
    result = 0

    f()
    
    for i in range(1, 2 * N + 1):
        if enemies[i] == float('inf'):
            continue

        if possible_counts[i] == 1:
            f()
        elif possible_counts[i] >= 2:
            # 가장 인원이 많은 곳 찾기
            possible_adjs = get_possible_adjacent_indexes(i)
            max_adj = None
            max_enemy = 0
            for adj in possible_adjs:
                if enemies[adj] > max_enemy:
                    max_adj = adj
                    max_enemy = enemies[adj]
            # 가장 인원이 많은 곳과 결합
            combine(i, max_adj)
            result += 1
        else:
            enemies[i] = float('inf')
            result += 1

    print(result)