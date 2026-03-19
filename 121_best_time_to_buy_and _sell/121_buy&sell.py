class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)

        return max_profit
# Time complexity: O(n) where n is the number of prices
# Space complexity: O(1) since we are using only a constant amount of space to store the minimum price and maximum profit.