import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int,input().split()))
    
    res = 0
    is_visited = [False]*(100001)
    j = 0
    for i in range(N):
        while(j < N):
            if(is_visited[nums[j]]): break
            is_visited[nums[j]] = True
            j += 1
        
        is_visited[nums[i]] = False
        res += j - i
    
    print(res)