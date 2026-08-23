class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        i = 0
        sum = 0

        while (sum <= n):
            i = i + 1
            sum = sum + i
        
        return i - 1