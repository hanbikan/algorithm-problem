from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def find_colons(strr):
    res = []
    for i in range(len(strr)):
        if strr[i] == ':':
            res.append(i)
    
    return res

strs = []
while True:
    strr = str(input().rstrip())
    if strr == "E":
        break
    
    colons = find_colons(strr)
    strs.append(strr[colons[0] + 1:colons[1]].replace('-', '.'))

for strr in strs:
    print("implementation(libs.{0})".format(strr))