class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""
        N = len(strs) #4

        min_len = min([len(s) for s in strs]) #3

        for idx in range(min_len): 
            set_idx = set([s[idx] for s in strs])
            if len(set_idx) == 1:
                res = res + list(set_idx)[0]
            else:
                break
        
        return res