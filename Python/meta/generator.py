import random

f = open("input.txt", "w")
T = random.randrange(1, 101)
f.write("{0}\n".format(T))
for _ in range(T):
    N = random.randrange(1, 101)
    M = random.randrange(0, N)
    f.write("{0} {1}\n".format(N, M))
    p = [str(random.randrange(1, 10)) for _ in range(N)]
    f.write("{0}\n".format(" ".join(p)))

f.close()