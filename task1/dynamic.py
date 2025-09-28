def find_min_coins(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    prev = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                prev[i] = coin

    result = {}
    current = amount
    while current > 0:
        coin = prev[current]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current -= coin

    return result