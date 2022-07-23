import sys
from typing import DefaultDict
from math import sqrt

input = sys.stdin.readline
MAX = 1000000000

def f(dic, n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            dic[n] -= 1

            dic[n//i] += 1
            f(dic, n//i)
            dic[i] += 1
            f(dic, i)
            return
    

if __name__ == '__main__':
    int(input())
    nums1 = list(map(int, input().split()))
    int(input())
    nums2 = list(map(int, input().split()))

    dict1 = DefaultDict(int)
    for n in nums1:
        dict1[n] += 1
        f(dict1, n)
    
    dict2 = DefaultDict(int)
    for n in nums2:
        dict2[n] += 1
        f(dict2, n)

    res = 1
    is_res_moded = False
    for k, v in dict1.items():
        if(dict2[k] > 0):
            res *= (k ** min(v, dict2[k]))
            if(res >= MAX):
                res %= MAX
                is_res_moded = True
    
    if(is_res_moded):
        print(
            "0"*(9 - len(str(res))) + str(res)
        )
    else:
        print(res)