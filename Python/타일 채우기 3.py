import sys
input = sys.stdin.readline

MOD = 1_000_000_007

N = int(input())

dp = [0,0,0,1]
for i in range(N):
    dp = [
        dp[3],
        (dp[2] + dp[3]) % 1_000_000_007,
        (dp[1] + dp[3]) % 1_000_000_007,
        (dp[0] + dp[1] + dp[2] + dp[3] * 2) % 1_000_000_007
    ]

print(dp[-1])
'''
0: 00
..
  

--
  

1: 01
--
 .

..
 .

.|
 |

2: 10
--
. 

..
. 

|.
| 

3: 11
..
..

--
..

..
--

--
--

|.
|.

.|
.|

||
||
'''
