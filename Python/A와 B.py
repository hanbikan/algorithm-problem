S = list(input())
T = list(input())

lenS = len(S)
while lenS < len(T):
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T = T[::-1]
if T == S:
    print(1)
else:
    print(0)
