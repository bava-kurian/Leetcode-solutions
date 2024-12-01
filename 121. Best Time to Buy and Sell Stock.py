class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        min_price = float('inf')
        
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_prof = max(max_prof, profit)
        
        return max_pro
