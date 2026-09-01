class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price=0
        for i in range(0,len(prices)):
            for j in range(i,len(prices)):
                if prices[i]<prices[j]:
                    price = prices[j]-prices[i]
                    max_price=max(max_price,price)
        return max_price

