# given an array of stock prices, we have to find out the max profit possible. if no profit possible return 0

def maxProfit(prices) -> int:
    max_profit=0
    for index, price in enumerate(prices):
        buy_price = price
        for j in range(index+1,len(prices)):
            if max_profit < (prices[j] - buy_price):
                # print(f"Buy price:{buy_price}")
                # print(f"Sell price:{prices[j]}\n")
                max_profit = prices[j]-buy_price
    return max_profit

print(maxProfit([10,1,5,6,7,1]))