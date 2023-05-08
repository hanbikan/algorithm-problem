import sys
input = sys.stdin.readline

'''
A가 홀수: A XOR A-1 XOR-1 반복
A가 짝수: B, 1, B+1, 0 반복
'''

def f(A, B):
    remainder = (B - A) % 4
    if A % 2 == 1:
        if remainder == 0: return A
        elif remainder == 1: return A ^ B
        elif remainder == 2: return A - 1
        else: return (A ^ B) - 1
    else:
        if remainder == 0: return B
        elif remainder == 1: return 1
        elif remainder == 2: return B + 1
        else: return 0

A, B = map(int, input().split())
print(f(A, B))