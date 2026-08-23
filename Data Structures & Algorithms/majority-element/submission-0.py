class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
            N = len(nums)
            mid = N // 2

            nums = sorted(nums)

            return nums[mid]