# Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#Naive Approach
#Time Limit Exceeded
# assuming buying at index 0 and sell at index 1 store all values in profit and get maximum profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=[] 
        for buyIndex in range(len(prices)):
            profitCurrent=0
            for sellIndex in range(buyIndex+1,len(prices)):
                if prices[sellIndex]-prices[buyIndex]>profitCurrent:
                    profitCurrent=prices[sellIndex]-prices[buyIndex]
            profit.append(profitCurrent)
        return(max(profit))

#Same Approach but with python tweaks
#Still Time Limit Exceeded
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for buyIndex in range(len(prices)-1):
            profitCurrent=max(prices[buyIndex+1:])-prices[buyIndex]
            profit=max(profit,profitCurrent)
        return(profit)