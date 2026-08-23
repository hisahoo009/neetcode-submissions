class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s = ''.join([char for char in s if char.isalnum()])

        i = 0
        j = len(s) - 1

        #print(s)

        while (i <= j):
            if s[i] != s[j]:
                return False
            if s[i] == s[j]:
                i = i + 1
                j = j - 1
        
        return True