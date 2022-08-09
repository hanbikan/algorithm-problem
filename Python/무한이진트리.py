import sys
input = sys.stdin.readline

if __name__ == '__main__':
    a, b = map(int, input().split())
    
    l, r = 0, 0
    while(not (a==1 and b==1)):
        if(a>b):
            t = (a-1)//b
            a = a - t*b
            l += t
        else:
            t = (b-1)//a
            b = b - t*a
            r += t

    print(l, r)