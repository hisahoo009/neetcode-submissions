class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        len_nums = len(nums)
        sumN = int((len_nums * (len_nums + 1))/2)

        sum_nums = sum(nums) # O(N)
        result = sumN - sum_nums

        return result