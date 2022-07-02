import sys
input = sys.stdin.readline
X, Y = 0, 1

def get_end_index(start_index):
    for i in range(start_index+1, n):
        if positions[i][X] != positions[start_index][X]:
            return i

    return n

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        positions = [list(map(int,input().split())) for _ in range(n)]
        positions.sort()
        
        res = []
        prev_start_y = 0
        i = 0
        while(i<n):
            end_index = get_end_index(i)

            to_added = sorted(positions[i:end_index], key=lambda x:x[1])
            if to_added[0][Y] != prev_start_y:
                to_added = to_added[::-1]

            res += to_added

            prev_start_y = res[-1][Y]
            i = end_index

        for index in list(map(int,input().split()))[1:]:
            print(*res[index-1])