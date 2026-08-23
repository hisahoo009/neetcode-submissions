import numpy as np

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        n = len(arr)
        if k == n:
            return sorted(arr)

        # arr = [2, 4, 5, 8]
        left = 0
        right = len(arr) - 1

        # l:1, r:3, r-l:2
        # l:1, r:2, r-l:1

        while (right - left) > (k - 1):
            a = arr[left]
            b = arr[right]
            
            if abs(a-x) < abs(b-x):
                right = right-1
            if abs(a-x) > abs(b-x):
                left = left+1
            
            if (abs(a-x) == abs(b-x)):
                right = right-1
        
        return sorted(arr[left:right+1])
            
        #2,3,4
        #l=0,r=2,k-1=2
        #

