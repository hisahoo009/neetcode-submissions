class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False

        arr = []
        curr = x

        while curr > 0:
            rem = curr % 10
            curr = curr // 10
            arr.append(rem)
        
        #print(arr)
        N = len(arr)
        left = 0
        right = N - 1

        while (left < right):
            
            if arr[left] != arr[right]:
                return False
            
            left = left + 1
            right = right - 1

        return True
