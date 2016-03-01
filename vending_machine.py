def give_change(amount):
    coins = [1, .50, .20, .10, .05, .02, .01]
    change = []
    for coin in coins:
        while coin <= amount:
            amount -= coin
            change.append(coin)
    return change

print give_change(1.73)