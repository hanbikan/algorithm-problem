import sys
input = sys.stdin.readline

N = int(input())
mans = list(map(int,input().split()))
girls = list(map(int,input().split()))

short_mans = []
tall_mans = []
for man in mans:
    if man > 0: short_mans.append(man)
    else: tall_mans.append(man)
short_mans.sort()
tall_mans.sort(reverse = True)

short_girls = []
tall_girls = []
for girl in girls:
    if girl > 0: short_girls.append(girl)
    else: tall_girls.append(girl)
short_girls.sort()
tall_girls.sort(reverse = True)

result = 0
tall_girl_index = 0
for short_man in short_mans:
    while tall_girl_index < len(tall_girls):
        if abs(tall_girls[tall_girl_index]) > short_man:
            tall_girl_index += 1
            result += 1
            break
        tall_girl_index += 1

tall_man_index = 0
for short_girl in short_girls:
    while tall_man_index < len(tall_mans):
        if abs(tall_mans[tall_man_index]) > short_girl:
            tall_man_index += 1
            result += 1
            break
        tall_man_index += 1

print(result)

'''
5
1 3 5 -3 -5
2 4 -1 -2 -3
'''