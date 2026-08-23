class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        N = len(nums)

        if N == 1:
            return True
        
        for i in range(1, N):
            s = nums[i] + nums[i-1]
            if s % 2 == 0:
                return False

        return True