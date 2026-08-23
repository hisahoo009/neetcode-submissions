class Solution:
    def maxScore(self, s: str) -> int:
        
        #000011101: 8
        #010101010: 

        ls, rs = s[0].count('0'), s[1: ].count('1')
        score = ls + rs

        N = len(s)

        for i in range(1, N-1):

            curr = s[i]
            if curr == '0':
                ls = ls + 1
            if curr == '1':
                rs = rs - 1

            sum = ls + rs
            if sum > score:
                #print("str: {}, index: {} and sum: {}".format(s, i, sum))
                score = sum
        
        return score