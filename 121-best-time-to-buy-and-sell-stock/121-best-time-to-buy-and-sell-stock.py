class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_diff = 0
        for i in prices:
            if i < buy:
                buy = i
            else:
                max_diff = max(max_diff,i-buy)
        return max_diff        
                
                