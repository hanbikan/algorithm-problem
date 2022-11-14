import sys
input = sys.stdin.readline

while True:
    n, m = map(float, input().split())
    if n == m == 0: break
    n = int(n)
    m = int(m*100)

    calories_and_prices = [[0,0]]
    for _ in range(n):
        c, p = map(float, input().split())
        c = int(c)
        p = int(p*100 + 0.5)
        calories_and_prices.append([c, p])

    dp = [0]*(m+1)
    for i in range(1, m+1):
        for j in range(1, n+1):
            calorie, price = calories_and_prices[j]

            if i - price >= 0:
                dp[i] = max(dp[i], dp[i-price] + calorie)
    
    print(dp[-1])