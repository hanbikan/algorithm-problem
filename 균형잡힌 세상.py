while True:
    strCur = input()
    if strCur == ".":
        break

    isBalanced = True
    stack = [-1]
    for c in strCur:
        if c == '(':
            stack.append(0)
        elif c == '[':
            stack.append(1)
        elif c == ')':
            if stack[-1] == 0:
                del stack[-1]
            else:
                isBalanced = False
                break
        elif c == ']':
            if stack[-1] == 1:
                del stack[-1]
            else:
                isBalanced = False
                break
    if isBalanced and stack != [-1]:
        isBalanced = False

    if isBalanced:
        print('yes')
    else:
        print('no')
