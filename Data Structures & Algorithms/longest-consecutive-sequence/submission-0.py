class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # check for elements 1 more or 1 less in hash
        # duplicate element - dont add to set
        # 0 
        # 3
        # 2 
        # 5 
        # 4
        # 6
        # 1

        st = set(nums)
        res = 0
        
        # O(N)
        for num in nums:

            if (num - 1) not in st:
                cur = num
                count = 0
                while cur in st:
                    cur = cur + 1
                    count = count + 1
                
                res = max(res, count)
        
        return res