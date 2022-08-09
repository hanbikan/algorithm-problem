import heapq
import sys
input = sys.stdin.readline


def getMergedCards(cards):
    newCard = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, newCard)
    heapq.heappush(cards, newCard)
    return cards


n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)

for _ in range(m):
    cards = getMergedCards(cards)

print(sum(cards))
