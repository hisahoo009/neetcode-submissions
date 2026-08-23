class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        # nums = -4,-1,-1,0,1,2
        
        N = len(nums)
        for i in range(N-2):
            rem = 0 - nums[i]
            j = i + 1
            k = N - 1
            while (j != k):
                sec = nums[j]
                third = nums[k]
                if (sec + third) < rem:
                    j = j + 1
                if (sec + third) > rem:
                    k = k - 1
                if (sec + third) == rem:
                    ins = [nums[i], sec, third]
                    j = j + 1
                    ins.sort()
                    if ins not in res:
                        res.append(ins)
        return res
                
