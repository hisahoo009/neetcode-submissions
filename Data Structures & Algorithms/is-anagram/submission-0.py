class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        Ns, Nt = len(s), len(t)
        s_new = sorted(s)
        t_new = sorted(t)

        if Ns != Nt:
            return False
        
        for ch_s, ch_t in zip(s_new, t_new):
            if ch_s != ch_t:
                return False
        
        return True
        
