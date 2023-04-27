import sys
input = sys.stdin.readline

S = str(input().rstrip())

# '3' '3' '(' '5' '6' '2' '(' '7' '1' '(' '9' ')'
# '3' '3' '(' '5' '6' '2' '(' '7' 1(as int)
# '3' '3' '(' '5' '6' 4(as int)
# '3' 18(as int)
# 19

stack = []
for c in S:
    if c == ')':
        q_length = 0
        while (len(stack) > 0):
            popped = stack.pop()
            if popped == '(':
                if len(stack) >= 1:
                    popped = stack.pop()
                    if '0' <= popped <= '9':
                        stack.append(int(popped) * q_length)
                    else: # "A(123)"
                        stack.append(q_length + 3)
                else: # "(123)"
                    stack.append(q_length + 2)
                break
            elif isinstance(popped, int):
                q_length += popped
            else:
                q_length += 1
    else:
        stack.append(c)

result = 0
while (len(stack) > 0):
    popped = stack.pop()
    if (isinstance(popped, int)):
        result += popped
    else:
        result += 1
print(result)