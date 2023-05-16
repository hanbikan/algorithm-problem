import sys
input = sys.stdin.readline

DIR_TO_INDEX = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

game_number = 1
while True:
    R, C = map(int, input().split())
    if R == C == 0: break
    mapp = [list(str(input().rstrip())) for _ in range(R)]
    
    x, y = -1, -1
    target_score = 0
    score = 0
    for i in range(R):
        for j in range(C):
            item = mapp[i][j]
            if item == 'w' or item == 'W':
                x, y = i, j
            if item == 'b' or item == 'B':
                target_score += 1
            if item == 'B':
                score += 1

    for c in str(input().rstrip()):
        nx, ny = x + dx[DIR_TO_INDEX[c]], y + dy[DIR_TO_INDEX[c]]
        nnx, nny = x + dx[DIR_TO_INDEX[c]] * 2, y + dy[DIR_TO_INDEX[c]] * 2
        next = mapp[nx][ny]
        if next == '.' or next == '+':
            if mapp[x][y] == 'W': mapp[x][y] = '+'
            else: mapp[x][y] = '.'
            if next == '+': mapp[nx][ny] = 'W'
            else: mapp[nx][ny] = 'w'
            x, y = nx, ny
        elif (0 <= nnx <= R - 1 and 0 <= nny <= C - 1) and (next == 'b' or next == 'B') and (mapp[nnx][nny] == '.' or mapp[nnx][nny] == '+'):
            if mapp[x][y] == 'W': mapp[x][y] = '+'
            else: mapp[x][y] = '.'
            if next == 'B':
                mapp[nx][ny] = 'W'
                score -= 1
            else: mapp[nx][ny] = 'w'
            if mapp[nnx][nny] == '+':
                mapp[nnx][nny] = 'B'
                score += 1
            else: mapp[nnx][nny] = 'b'
            x, y = nx, ny
        if score == target_score:
            break
    
    print("Game {0}: {1}".format(game_number, "complete" if score == target_score else "incomplete"))
    for line in mapp:
        print(''.join(line))
    
    game_number += 1

'''
문자	뜻
.	빈 공간
#	벽
+	비어 있는 목표점
b	박스
B	목표점 위에 있는 박스
w	캐릭터
W	목표점 위에 있는 캐릭터
'''