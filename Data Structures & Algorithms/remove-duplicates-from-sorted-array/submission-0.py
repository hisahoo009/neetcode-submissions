class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k, i = 1, 1
        N = len(nums)
        prev = nums[0]

        #[1,1,2,3,4]
        # N=5
        #
        while (i < N):
            
            if i >= len(nums):
                break
            
            if i < len(nums):
                curr = nums[i]
                if curr == prev:
                    del nums[i]
                    continue
                
                if curr != prev:
                    k = k + 1
                    i = i + 1
                    prev = curr

        return k