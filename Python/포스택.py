import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
tops = [0] * 4

is_possible = True
for num in nums:
    flag = False
    for i in range(4):
        if num > tops[i]:
            tops[i] = num
            flag = True
            break
    
    if not flag:
        is_possible = False
        break

print("YES") if is_possible else print("NO")