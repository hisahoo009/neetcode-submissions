class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        N = len(heights)
        max_vol = 0

        # O(N^2)
        for i in range(N-1):
            for j in range(i+1, N):
                vol = min(heights[j], heights[i]) * (j-i)
                if vol > max_vol:
                    max_vol = vol
        
        return max_vol