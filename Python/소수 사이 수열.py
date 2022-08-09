from bisect import bisect_left
from math import sqrt
import sys
input = sys.stdin.readline
MAX = 1299709

def check_is_prime_number(number):
    for i in range(2, int(sqrt(number) + 1)):
        if number % i == 0:
            return False

    return True

def set_is_prime_number(number):
    global is_prime_number
    if is_prime_number[number]:
        if check_is_prime_number(number):
            for i in range(number*2, MAX+1, number):
                is_prime_number[i] = False
            return True

    return False

def get_prime_numbers():
    global is_prime_number
    res = []
    is_prime_number = [True]*(MAX+1)
    
    for i in range(2, MAX+1):
        if set_is_prime_number(i):
            res.append(i)
    
    return res

if __name__ == '__main__':
    prime_numbers = get_prime_numbers()

    for _ in range(int(input())):
        k = int(input())
        index = bisect_left(prime_numbers, k)
        if(prime_numbers[index] == k):
            print(0)
        else:
            print(prime_numbers[index] - prime_numbers[index-1])