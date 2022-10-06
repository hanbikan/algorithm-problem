
def f(z, o, K, X):
    if (z//K)*(X - K) < o: return -1
    else:
        # 1 -1 / 1 3
        return max(0, (z + o - 1) // X + 1)

for i in range(1, 10):
    for j in range(1, 6):
        print(i, j, f(i, j, 3, 5))
