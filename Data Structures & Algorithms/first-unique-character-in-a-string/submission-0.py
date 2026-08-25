class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        ch_dict = {}

        for ch in s:
            ch_dict[ch] = (ch_dict[ch] + 1) if (ch in ch_dict.keys()) else 1

        unique_vals = [k for k, v in ch_dict.items() if v == 1]

        #print(unique_vals)
        for idx, ch in enumerate(s):
            if ch in unique_vals:
                return idx
        
        return -1