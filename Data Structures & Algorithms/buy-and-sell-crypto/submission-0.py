class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float("inf")
        l, maxP = 0, 0

        for r in range(len(prices)):
            maxP = max(maxP, prices[r] - minPrice)
            while minPrice > prices[r]:
                minPrice = min(minPrice, prices[l])
                l += 1
        return maxP
        