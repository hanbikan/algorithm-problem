import sys
input = sys.stdin.readline

def f(n):
    if n % 5 == 2 or n % 5 == 0:
        return "CY"
    else:
        return "SK"

N = int(input())
print(f(N))

'''
1 2 3 4 5 6 7 8 9 10
S C S S C S C S S C
1 S
= 1

2 C
= 1 + 1

3 S(1 + 1 + 1)
= 1 + 1 + 1

4 S(4)
= 4

5 C
= 4 + 1

6 S(1 + 1 + 4)
= 4 + 1 + 1

7 C
= 4 + 1 + 1 + 1

8 S
= 4 + 4 = 4 + 1 + 1 + 1 + 1

9 S
= 4 + 4 + 1(S) = 4 + 1 + 1 + 1 + 1 + 1(C) = 1 * 9(S)

10 C
= 4 + 4 + 1 + 1(C) = 4 + 1 + 1 + 1 + 1 + 1 + 1(S) = 1 * 10(C)
'''