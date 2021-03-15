import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

RET = 0
curMoney = K
while curMoney > 0:
    curMaxCoin = coins.pop()
    RET += curMoney // curMaxCoin
    curMoney = curMoney % curMaxCoin

print(RET)
