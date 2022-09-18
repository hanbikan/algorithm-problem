import sys
input = sys.stdin.readline

# len: 3~15
# -_.
# .은 연속 사용, 처음과 끝 불가




def solution(new_id):
    res = list(new_id)
    # 1
    for i in range(len(res)):
        if 'A' <= res[i] <= 'Z':
            res[i] = chr(ord(res[i]) - (ord('A') - ord('a')))
        

    # 2
    next_res = []
    for i in range(len(res)):
        if 'a' <= res[i] <= 'z' or '0' <= res[i] <= '9' or res[i] == '.' or res[i] == '-' or res[i] == '_':
            next_res.append(res[i])
    res = next_res

    # 3
    next_res = [res[0]]
    for i in range(1, len(res)):
        if res[i-1] == '.' and res[i] == '.': continue
        next_res.append(res[i])
    res = next_res

    # 4
    if len(res) > 0 and res[0] == '.': res = res[1:]
    if len(res) > 0 and res[-1] == '.': res = res[:len(res)-1]

    # 5
    if len(res) == 0:
        res = ['a']
    
    # 6
    if len(res) >= 16:
        res = res[:15]
        if res[-1] == '.': res = res[:len(res)-1]
    
    # 7
    if len(res) <= 2:
        while len(res) < 3:
            res.append(res[-1])

    return ''.join(res)

new_id = str(input().rstrip())
print(solution(new_id))