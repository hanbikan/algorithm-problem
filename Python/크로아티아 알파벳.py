word = input()
i=0
RET = 0
while i<len(word):
    RET+=1
    if i+1 <= len(word)-1:
        if word[i]=='c' and word[i+1]=='=':
            i+=2
            continue
        elif word[i]=='c' and word[i+1]=='-':
            i+=2
            continue
        elif word[i]=='d' and word[i+1]=='-':
            i+=2
            continue
        elif word[i]=='l' and word[i+1]=='j':
            i+=2
            continue
        elif word[i]=='n' and word[i+1]=='j':
            i+=2
            continue
        elif word[i]=='s' and word[i+1]=='=':
            i+=2
            continue
        elif word[i]=='z' and word[i+1]=='=':
            i+=2
            continue
    if i+2 <= len(word)-1:
        if word[i]=='d' and word[i+1]=='z' and word[i+2]=='=':
            i+=3
            continue
    i+=1
print(RET)