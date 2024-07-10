import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

odd_cards = []
even_cards = []

for i in range(N):
    if i % 2 == 0:
        odd_cards.append(cards[i])
    else:
        even_cards.append(cards[i])

cur_sum = sum(even_cards)
result = cur_sum
# 내 턴에 밑장 빼기
for i in range(N // 2):
    cur_sum += odd_cards[i] - even_cards[i]
    result = max(result, cur_sum)

# 상대 턴에 밑장 빼기
cur_sum = sum(odd_cards)
result = max(result, cur_sum)
for i in range(N // 2 - 1, 0, -1):
    cur_sum += even_cards[i - 1] - odd_cards[i]
    result = max(result, cur_sum)

print(result)

'''
10
1 2 3 4 5 6 7 8 9 10

1 3 5 7 9
2 4 6 8 10

<내 턴에 밑장 빼기>
2 4 6 8 10
1 4 6 8 10
1 3 6 8 10
1 3 5 8 10
1 3 5 7 10
1 3 5 7 9

<상대 턴에 밑장 뺴기>
1 2 4 6 8
1 3 4 6 8
1 3 5 6 8
1 3 5 7 8
1 3 5 7 9
'''