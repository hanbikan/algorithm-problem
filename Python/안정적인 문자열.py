import sys
input = sys.stdin.readline

i = 1
while True:
    strr = str(input().rstrip())
    if strr[0] == '-': break

    stack = []
    for c in strr:
        if c == '}' and len(stack) >= 1 and stack[-1] == '{':
            stack.pop()
        else:
            stack.append(c)
    res = 0

    while len(stack) > 0:
        a, b = stack.pop(), stack.pop()
        # }{
        if a == '{' and b == '}': res += 2
        # {{ }}
        else: res += 1

    print(f'{i}. {res}')
    i += 1