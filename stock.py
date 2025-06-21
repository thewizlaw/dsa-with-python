def main():
    prices = [7,1,5,3,6,4]
    s = stock(prices)
    print(s)


def stock(prices):
    buy = prices[0]
    profit = 0
    curr_profit = 0
    n = len(prices)

    for i in range(1, n):
        if prices[i] < buy:
            buy = prices[i]
            print("buy", buy)
        else:
            curr_profit = prices[i] - buy
            print("current:", curr_profit)
            profit = max(curr_profit, profit)

    return profit

main()
        
