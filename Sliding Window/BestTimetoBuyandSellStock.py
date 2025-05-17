# Pattern: Sliding Window (Min tracking)
# Link: Best Time to Buy and Sell Stock
# Difficulty: Easy (but conceptually critical — comes up in interviews constantly)

# Problem:
# You're given an array prices[] where prices[i] is the stock price on day i.
# You want to buy once and sell once to maximize profit.
# Return the max profit you can achieve. If no profit is possible, return 0.

# def maxProfit(prices):
#     max_profit = 0
#     min_price = float('inf')

#     for price in prices:
#         profit = price - min_price
#         max_profit = max(max_profit, profit)
#         min_price = min(min_price, price)

#     return max_profit

# print(maxProfit([7, 1, 5, 3, 6, 4])) # Expected: 5  (Buy at 1, Sell at 6)