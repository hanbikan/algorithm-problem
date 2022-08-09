import sys, bisect
input = sys.stdin.readline

if __name__ == '__main__':
    dp = [1,2]
    index_to_replace = 0
    prev = [1, 2]
    while(True):
        sm = sum(prev)
        dp.append(sm)
        prev[index_to_replace] = sm
        index_to_replace = (index_to_replace + 1)%2
        if sm > 10**100:
            break

    while(True):
        a, b = map(int, input().split())
        if(a == 0 and b == 0): break
        
        res = bisect.bisect_right(dp, b) - bisect.bisect_left(dp, a)
        print(res)