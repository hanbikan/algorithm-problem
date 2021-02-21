N = int(input())
for i in range(N):
    cur = input()
    idxCur = 0 #100+1+ 또는 01의 시작 부분을 가리키도록 설계
    prtCur = 'YES'
    while idxCur < len(cur):
        if cur[idxCur]=='0':
            if idxCur+1<len(cur) and cur[idxCur+1]=='1':
                idxCur+=2
            else:
                prtCur = 'NO'
                break
        elif cur[idxCur]=='1':
            try:
                if idxCur+2<len(cur) and cur[idxCur+1]=='0' and cur[idxCur+2]=='0':
                    idxCur+=3
                else:
                    prtCur = 'NO'
                    break

                if cur[idxCur]=='0': #0+의 경우
                    while idxCur<len(cur) and cur[idxCur]=='0':
                        idxCur+=1

                if cur[idxCur]=='1':
                    idxCur+=1
                else:
                    prtCur = 'NO'
                    break
                if idxCur<len(cur) and cur[idxCur]=='1':
                    while idxCur<len(cur) and cur[idxCur]=='1':
                        idxCur+=1
                    if idxCur+1<len(cur):
                        if cur[idxCur+1]=='0':
                            idxCur-=1
                        elif cur[idxCur+1]=='1':
                            idxCur+=2
            except:
                prtCur = 'NO'
                break

    print(prtCur)