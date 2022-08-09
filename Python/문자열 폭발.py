s=input()
BOMB=input()
lenBomb=len(BOMB)
stack=[]
for i in range(len(s)):
    stack.append(s[i])
    if(s[i]==BOMB[-1] and ''.join(stack[-lenBomb:])==BOMB):
        del stack[-lenBomb:]
if stack: print(''.join(stack))
else: print('FRULA')