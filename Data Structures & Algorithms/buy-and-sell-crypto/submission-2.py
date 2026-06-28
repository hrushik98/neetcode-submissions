class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l+1
        max_profit = 0
        
        while l <len(prices) and  r < len(prices):
            cur_profit = prices[r] -prices[l]
            if cur_profit < 0:
                l = r
                r = r+1
            elif cur_profit > 0:
                if cur_profit < max_profit:
                    r += 1
                elif cur_profit > max_profit:
                    max_profit = cur_profit
                    r+=1
                elif cur_profit == max_profit:
                    r+=1
            elif cur_profit == 0:
                r+=1
        return max_profit
            
        