# Pattern: Sliding Window (Min tracking)
# Link: Best Time to Buy and Sell Stock
# Difficulty: Easy (but conceptually critical — comes up in interviews constantly)

# Problem:
# You're given an array prices[] where prices[i] is the stock price on day i.
# You want to buy once and sell once to maximize profit.
# Return the max profit you can achieve. If no profit is possible, return 0.

# def MaxProfit(prices):
#     max_profit = 0
#     min_price =  float('inf')

#     for price in prices:
#         profit = price - min_price
#         max_profit = max(max_profit , profit)
#         min_price = min(min_price, price)

#     return max_profit

# print(MaxProfit([7, 1, 5, 3, 6, 4]))

# More Drilling Attemps Below ---------------------------------------------

# def MaxProfits(prices):
#     max_profit = 0 # This is defining the variable of max_profit as we need to track the max profit for the question, since its asking for it.
#     min_price = float('inf') # This is tracking the minimum price as we want to find the minimum price when we are iterating through the array. And we use a float incase of a dcimal as well as infinite depending on how low the int goes.

#     for price in prices: # We are for looping over the entire array.
#         profit = price - min_price # We are calcualting the prfit which is gonna be iterable price minus the min_price at the time of iterating. Basically subtracting the price of what we bought with the min_price of what we could buy it at to find the profit.
#         max_profit = max(max_profit, profit) #We are not figuring out the max profit that can be made comparing max_profit which is 0 and profit, which is calcuated earlier, and then assigning that to the new max_profit.
#         min_price = min(min_price, price) # We are calculating the min price here now.

#     return max_profit

# def MaxProfit(prices):
#     max_profit = 0
#     min_price = float('inf')

#     for price in prices:
#         profit = price - min_price
#         max_profit = max(max_profit, profit)
#         min_price = min(min_price, price)

#     return max_profit






