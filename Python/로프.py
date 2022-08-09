N = int(input())
ropes = []
for _ in range(N): ropes.append(int(input()))
ropes.sort(reverse=True)
maxWeight = 0
for i in range(len(ropes)):
    maxWeight = max(maxWeight, ropes[i]*(i+1))
print(maxWeight)