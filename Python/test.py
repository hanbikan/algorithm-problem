from math import sqrt


for t in range(1, 100):
    res = []
    i = 1
    while 2*i+1 <= t:
        if sqrt(t + i**2) % 1 == 0:
            res.append(int(sqrt(t + i**2)))
        i += 1

    if len(res) == 0: res.append(-1)
    print(t, res)