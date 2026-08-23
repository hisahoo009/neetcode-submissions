class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        
        N = len(nums)

        if N == 0:
            return [[lower, upper]]

        new_nums = [lower] + nums + [upper]
        res = []

        for i in range(1, N+2):
            low = (new_nums[i-1] + 1) if (i > 1) else new_nums[i-1]
            up = (new_nums[i] - 1) if (i < (N+1)) else new_nums[i]

            print(low, up)

            if low <= up:
                sub_range = [low, up]
                res.append(sub_range)
        
        return res