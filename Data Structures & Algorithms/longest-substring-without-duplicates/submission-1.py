class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # "abcdecfgh"
        curr_str = ''
        curr_length, max_length = 0, 0 

        for idx, curr in enumerate(s):
            if curr not in curr_str:
                curr_length = curr_length + 1
                curr_str = curr_str + curr
                continue
            
            if curr in curr_str:
                max_length = curr_length if (curr_length > max_length) else max_length
                # idx of last element with value curr
                indices = [i for i in range(len(s[:idx])) if s[i]==curr]
                # refresh curr_str and curr_length
                #print(idx)
                #print(curr_str)
                #print(indices)
                curr_str = s[(indices[-1]+1):(idx+1)] 
                curr_length = len(curr_str)
        
        max_length = curr_length if (curr_length > max_length) else max_length
        return max_length