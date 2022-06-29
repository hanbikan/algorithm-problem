import sys
input = sys.stdin.readline

if __name__ == '__main__':
    strr = str(input().rstrip())

    res = 0
    boshy_count = 0
    for i in range(len(strr)-1):
        if strr[i] == '(' and strr[i+1] == '(':
            boshy_count += 1

        if strr[i] == ')' and strr[i+1] == ')':
            res += boshy_count
    
    print(res)