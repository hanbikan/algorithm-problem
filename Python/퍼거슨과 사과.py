from math import gcd
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    R, G = map(int, input().split())
    g = gcd(R, G)
    for i in range(1, int(pow(g, 0.5))+1):
        if(g%i == 0):
            print(i, R//i, G//i)
            i2 = g//i
            if(i != i2):
                print(i2, R//i2, G//i2)