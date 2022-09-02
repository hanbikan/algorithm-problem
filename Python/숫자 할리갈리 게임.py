from collections import deque
from re import S
from sre_constants import GROUPREF
import sys
input = sys.stdin.readline
DO, SU, DRAW = 0, 1, 2

def f():
    global decks
    grounds = [deque(), deque()]
    turn = DO

    for _ in range(M):
        grounds[turn].append(decks[turn].pop())
        if len(decks[turn]) == 0:
            break

        # 종 치는 조건 체크
        if (len(grounds[DO]) != 0 and grounds[DO][-1] == 5) or (len(grounds[SU]) != 0 and grounds[SU][-1] == 5):
            # DO 승리
            # 그라운드에 나와 있는 각각의 카드 더미에서 가장 위에 위치한 카드의 숫자가 5가 나오는 순간 도도가 종을 친다.
            while len(grounds[SU]) > 0:
                decks[DO].appendleft(grounds[SU].popleft())
            while len(grounds[DO]) > 0:
                decks[DO].appendleft(grounds[DO].popleft())
        elif (len(grounds[DO]) != 0 and len(grounds[SU]) != 0) and grounds[DO][-1] + grounds[SU][-1] == 5:
            # SU 승리
            # 그라운드에 나와 있는 각각의 카드 더미에서 가장 위에 위치한 카드의 숫자 합이 5가 되는 순간 수연이가 종을 친다. 단, 어느 쪽의 그라운드도 비어있으면 안된다.
            while len(grounds[DO]) > 0:
                decks[SU].appendleft(grounds[DO].popleft())
            while len(grounds[SU]) > 0:
                decks[SU].appendleft(grounds[SU].popleft())

        if len(decks[DO]) == 0 or len(decks[SU]) == 0:
            break
        
        turn = (turn + 1) % 2
    
    if len(decks[DO]) > len(decks[SU]):
        return DO
    elif len(decks[SU]) > len(decks[DO]):
        return SU
    else:
        return DRAW

N, M = map(int,input().split())
decks = [deque(), deque()]

for _ in range(N):
    a, b = map(int,input().split())
    decks[DO].append(a)
    decks[SU].append(b)

res = f()
if (res == DO): print("do")
elif (res == SU): print("su")
else: print("dosu")