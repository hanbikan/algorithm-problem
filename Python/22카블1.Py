import sys
input = sys.stdin.readline

class Date:
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

    def add_month(self, month):
        nm = self.m + month
        self.m = nm % 12
        self.y += nm // 12

    def add_27_days(self):
        nd = self.d + 27
        self.d = nd % 28
        nm = self.m + nd // 28
        self.m = nm % 12
        self.y += nm // 12
        

def string_to_date(strr):
    y = int(strr[0:4])
    m = int(strr[5:7]) - 1
    d = int(strr[8:10]) - 1
    return Date(y, m, d)

def compare(date1, date2):
    d1 = date1.y*10000 + date1.m*100 + date1.d
    d2 = date2.y*10000 + date2.m*100 + date2.d
    if d1 > d2: return -1
    elif d1 == d2: return 0
    else: return 1

def solution(today, terms, privacies):
    res = []
    parsed_today = string_to_date(today)

    term_to_month = {}
    for term in terms:
        t, m = term.split(' ')
        term_to_month[t] = int(m)

    for i in range(len(privacies)):
        date, term = privacies[i].split(' ')
        parsed_date = string_to_date(date)
        month_to_add = term_to_month[term]
        parsed_date.add_month(month_to_add-1)
        parsed_date.add_27_days()
        if compare(parsed_date, parsed_today) == 1:
            res.append(i+1)
    return res

# 1, 4, 5
print(solution(
    "2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
))

print(solution(
    today = "2022.05.19",
    terms = ["A 6", "B 12", "C 3"],
    privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
))
