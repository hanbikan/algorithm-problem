import sys
input = sys.stdin.readline

def f(num_as_string):
    length = len(num_as_string)
    for r in range((length + 1) // 2, length):
        l = length - 1 - r
        left, right = num_as_string[l], num_as_string[r]
        if left != right:
            if int(left) > int(right):
                num_as_string = num_as_string[:r] + num_as_string[:l + 1][::-1]

            else:
                new_num_as_string = str(int(num_as_string[:r]) + 1) + num_as_string[:l + 1][::-1]
                return f(new_num_as_string)
    return num_as_string

N = int(input())
N += 1
print(f(str(N)))

'''
TEST = int(input())
t = TEST
while True:
    t += 1
    strr = str(t)
    is_p = True
    for j in range(len(strr) // 2):
        if strr[j] != strr[len(strr) - 1 - j]:
            is_p = False
            continue
    if is_p:
        print(t)
        break
'''