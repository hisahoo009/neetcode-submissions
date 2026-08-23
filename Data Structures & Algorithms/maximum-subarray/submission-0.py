class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    
        max_sum = nums[0]
        running_sum = nums[0]

        for num in nums[1: ]:
        
            if (num + running_sum) > num:
                running_sum = num + running_sum

            else:
                if (num + running_sum) <= num:
                    running_sum = num
        
            if max_sum < running_sum:
                max_sum = running_sum

        return max_sum

        # 2,-3,4,-2,2,1,-1,4
        # 2,2
        # -1, 2
        # 4, 4
        # 2,4
        # 4,4
        # 5,5
        # 4,5
        # 8,8


