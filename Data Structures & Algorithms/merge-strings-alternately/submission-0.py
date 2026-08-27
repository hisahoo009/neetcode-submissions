class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        N1, N2 = len(word1), len(word2)
        minN = min(N1, N2)

        i = 0
        out = ''

        while (i < minN):
            out = out + word1[i] + word2[i]
            i = i + 1
        
        if (i == N1) and (i < N2): # word1 is complete, word2 remains
            out = out + word2[i: ]
        if (i == N2) and (i < N1): # word2 is complete, word1 remains
            out = out + word1[i: ]
        
        return out
        