import sys
input = sys.stdin.readline

if __name__ == '__main__':
  for _ in range(int(input())):       
    # Input
    p = str(input().rstrip())
    n = int(input())              
    if n == 0:
      input()
      nums = []
    else:    
      nums = [int(c) for c in str(input().rstrip())[1:-1].split(',')]      
    
    # Solution
    is_successful = True
    is_reversed = False
    left, right = 0, n # A range to print
    for c in p:
      if c == 'R':
        is_reversed = not is_reversed
      else:
        if left == right:
          is_successful = False
          break

        if not is_reversed:
          left += 1
        else:
          right -= 1

    # Print
    if is_successful:
      if not is_reversed:      
        print("[" + ",".join(map(str, nums[left:right])) + "]")
      else:    
        print("[" + ",".join(map(str, nums[left:right][::-1])) + "]")
    else:
      print("error")
