from copy import deepcopy
import sys
input = sys.stdin.readline

discounts = [10, 20, 30, 40]

def f(nums, cur, left):
    if left == 0: return [cur]

    res = []
    for i in range(len(nums)):
        res += f(nums, cur + [nums[i]], left - 1)
    return res

def solution(users, emoticons):
    res = [0, 0]
    e_len = len(emoticons)

    for cur_discounts in f(discounts, [], e_len):
        cur_emoticons = deepcopy(emoticons)
        for i in range(e_len):
            cur_emoticons[i] = int(cur_emoticons[i] * (100 - cur_discounts[i]) / 100)
        
        total_joined = 0
        total_price = 0

        for ud, up in users:
            user_price = 0
            has_joined = False

            for i in range(e_len):
                if ud <= cur_discounts[i]:
                    user_price += cur_emoticons[i]

            if up <= user_price:
                user_price = 0
                has_joined = True
            
            if has_joined: total_joined += 1
            total_price += user_price
        
        if total_joined > res[0]:
            res = [total_joined, total_price]
        elif total_joined == res[0]:
            if total_price > res[1]:
                res = [total_joined, total_price]
        
    return res

            

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
#print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))