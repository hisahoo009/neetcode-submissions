class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        res = 0

        N = len(nums)
        running_sum = nums[0]
        
        for i in range(1, N):
            
            curr = nums[i]
            prev = nums[i-1]

            if curr > prev:
                running_sum = running_sum + curr
            
            if curr <= prev:
                res = max(res, running_sum)
                running_sum = curr
                prev = curr
        
        res = max(res, running_sum)
        return res

