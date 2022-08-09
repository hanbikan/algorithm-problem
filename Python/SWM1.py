def main():
    x = input()
    cnt1, cnt2 = 0, 0
    for cur in x:
        if cur=='(': cnt1+=1
        elif cur==')': cnt2+=1
    if cnt1==cnt2: print('YES')
    else: print('NO')

if __name__=="__main__":
    main()