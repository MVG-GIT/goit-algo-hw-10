def find_coins_greedy(amount, coins):
    coins.sort(reverse=True)
    
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result