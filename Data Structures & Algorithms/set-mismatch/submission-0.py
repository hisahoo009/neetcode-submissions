class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        N = len(nums)
        sum_set = sum(set(nums)) # S - missing
        sum_nums = sum(nums) # S - missing + rep
        correct_sum = (N * (N+1)) // 2

        missing = correct_sum - sum_set
        rep = sum_nums - correct_sum + missing

        return [rep, missing]
