def solution(k, datum):
    cases=[ [[datum, 0]] ]
    for i in range(0, k):
        newCases=[]
        for c in range(len(cases[i])): #case trace
            for j in range(len(cases[i][c][0])-1): #파일 용량들 trace
                new_datum=cases[i][c][0][:j]
                new_datum.append(cases[i][c][0][j]+cases[i][c][0][j+1])
                if len(cases[i][c][0])-1 >= j+2: new_datum+=cases[i][c][0][j+2:]
                newCases.append([new_datum,cases[i][c][1]+cases[i][c][0][j]+cases[i][c][0][j+1]])

        cases.append(newCases)
    print(cases[i])

#solution(4, [40, 30, 30, 50])
solution(15, [1,21,3,4,5,35,5,4,3,5,98,21,14,17,32])