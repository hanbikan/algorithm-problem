import sys
read = sys.stdin.readline
i=1
while True:
    P, L, V = map(int, read().strip().split())
    if P==L==V==0: break
    print("Case {}: {}".format(i, (V//L)*P + min(V%L, P)))
    i+=1