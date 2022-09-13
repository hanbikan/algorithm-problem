import sys
input = sys.stdin.readline

def f():
    x, y = map(int,input().split())
    z = x + y

    last_sum = 0
    index = 1
    while True:
        to_add = last_sum + index

        if to_add > z: break
        elif to_add == z:
            last_sum = to_add
        else:
            last_sum = to_add
            index += 1
        
    if last_sum != z: return -1

    res = 0
    for i in range(index, 0, -1):
        if x - i >= 0:
            x -= i
            res += 1

            if x == 0: break
    
    return res

print(f())