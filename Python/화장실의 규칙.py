from queue import PriorityQueue
import sys
input = sys.stdin.readline
D, H, Y, X = 0, 1, 2, 3

def put_info(x,y):
    pq.put((-info[x][y][D], -info[x][y][H], info[x][y][Y], info[x][y][X]))

def get_info():
    res = pq.get()
    return -res[0], -res[1], res[2], res[3]

if __name__ == '__main__':
    N, M, K = map(int,input().split())

    info = [[None]*M for _ in range((N-1)//M+1)]

    for i in range(N):
        x, y = i // M, i % M
        d, h = map(int, input().split())
        info[x][y] = [d,h,y,x]

    pq = PriorityQueue()
    for i in range(min(M, N)):
        put_info(0,i)

    res = 0
    my_x, my_y = K // M, K % M
    while(not pq.empty()):
        d,h,y,x = get_info()

        if(x==my_x and y==my_y):
            print(res)
            break

        # Possibly there is no elem after current item
        if(x+1 <= len(info)-1 and info[x+1][y] != None):
            put_info(x+1, y)
        
        res += 1