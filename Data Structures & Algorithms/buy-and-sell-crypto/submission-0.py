class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        lowest_price=prices[0]
        for day in range(1,len(prices)):
            profit=prices[day]-lowest_price
            max_profit=max(max_profit,profit)
            lowest_price=min(lowest_price,prices[day])
        return max_profit