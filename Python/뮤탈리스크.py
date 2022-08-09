from itertools import permutations
import sys
input = sys.stdin.readline

def f():
    q = [health]
    visited = set()
    visited.add(tuple(health))
    count = 1
    
    while (len(q) > 0):
        nq = []
        while (len(q) > 0):
            cur = q.pop()
            for next_tuple in permutations(cur):
                next_list = list(next_tuple)
                
                to_remove = 9
                is_dead = True
                for i in range(N):
                    next_list[i] = max(0, next_list[i] - to_remove)
                    if (next_list[i] > 0): is_dead = False
                    to_remove //= 3

                if (is_dead): return count
                if (tuple(next_list) in visited): continue

                visited.add(tuple(next_list))
                nq.append(next_list)
        q = nq
        count += 1

if __name__ == '__main__':
    N = int(input())
    health = list(map(int,input().split()))

    print(f())