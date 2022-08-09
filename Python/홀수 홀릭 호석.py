import sys
input = sys.stdin.readline

def f(st):
    res = [0,0]
    for i in range(len(st)):
        if(int(st[i]) % 2 == 1):
            res[0] += 1
    res[1] = res[0];
                 
    # Cut
    if(len(st) >= 2):
        if(len(st) == 2):
            nextInt = int(st[0]) + int(st[1])

            t1, t2 = f(str(nextInt))
            res[0] += t1
            res[1] += t2
        else:
            # 3분할에 대해 브루트포스
            minRes, maxRes = float('inf'), 0

            # s, e: 가운데 문자열 범위
            for s in range(1, len(st) - 1):
                for e in range(s+1, len(st)):
                    nextInt = int(st[0:s]) + int(st[s:e]) + int(st[e:len(st)])

                    t1, t2 = f(str(nextInt))
                    minRes = min(minRes, t1)
                    maxRes = max(maxRes, t2)

            res[0] += minRes
            res[1] += maxRes

    return res

def solution():
    N = str(input().rstrip())
    print(*f(N))

if __name__ == '__main__':
    solution()                            