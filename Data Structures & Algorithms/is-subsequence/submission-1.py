class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # s=node
        # t=neetcode
        # dt={0:n,1:e,2:e,3:t,4:c,5:o,6:d,7:e}
        dt = {}
        for idx, ch in enumerate(t):
            dt[idx] = ch

        pos = -1
        for ch in s:
            if ch in dt.values():
                all_pos = [key for key, val in dt.items() if val==ch]
                all_pos = sorted(all_pos)

                # find idx > pos, if no idx > pos, return False
                if all_pos[-1] <= pos:
                    return False
                
                for idx in all_pos:
                    if idx > pos:
                        pos = idx
                        break
    
            if ch not in dt.values():
                return False
        
        return True

        # ch=n, all_pos=[0], pos=0
        # ch=o, all_pos=[5], pos=5
        # ch=d, all_pos=[6], pos=6
        # ch=e, all_pos=[1,2,7], pos=7

        # dt={0:g,1:e,2:e,3:k,4:s,5:f,6:o,7:r,8:g,9:e,10:e,11:k,12:s}
        # s=gfk
        # ch=g, ap=[0,8]