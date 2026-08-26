class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        # practice: 0, coding: 3, N: 5, dist = abs(j-i)
        # makes: [1,4], coding: [3], N: 5, dist = 2, 1
        
        N = len(wordsDict)
        
        word1_indices = [idx for idx, word in enumerate(wordsDict) if word == word1]
        word2_indices = [idx for idx, word in enumerate(wordsDict) if word == word2]

        dists = []
        for i in word1_indices:
            for j in word2_indices:
                dists.append(abs(i-j))
        
        return min(dists)

