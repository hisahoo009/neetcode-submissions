class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # min_idx = 0, max_diff = -200
        # 0, diff = prices[idx] - prices[min_idx] = 0, 0
        # 1, 0, 0
        # 1, 4, 4
        # 1, 5, 5
        # 1, 6, 6
        # 1, 0, 6

        # 0, 0, 0
        # 1, 0, 0

        min_idx = 0
        max_diff = -200

        for idx in range(len(prices)):
            if prices[min_idx] > prices[idx]:
                min_idx = idx
            
            diff = prices[idx] - prices[min_idx]

            if diff > max_diff:
                max_diff = diff
        
        return max_diff