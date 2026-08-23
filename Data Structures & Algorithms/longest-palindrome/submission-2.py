from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        # {a:1, b:1, c:4, d:2}
        # n % 2 == 1: 
        char_dict = dict(Counter(s))
        print(char_dict)
        res = 0
        
        for k, v in char_dict.items():
            sub = v if (v % 2 == 0) else (v-1)
            char_dict[k] = v - sub
            res = res + sub
        
        if 1 in char_dict.values():
            res = res + 1
        
        return res

