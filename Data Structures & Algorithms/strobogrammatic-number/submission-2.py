class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        strob_dict = {'1': '1', '2': None, '3': None, '4': None, '5': None, '6': '9', '7': None, '8': '8', '9': '6', '0': '0'}
        N = len(num)
        left = ((N + 1) // 2) - 1
        right = (N // 2)

        while (left != -1 and right != N):
            if num[left] != strob_dict[num[right]]:
                return False
            left = left - 1
            right = right + 1
        
        return True