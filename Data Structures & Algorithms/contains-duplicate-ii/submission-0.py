class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        N = len(nums)
        setN = len(set(nums))

        if N == setN:
            return False
        
        _dict = {}

        # O(N)
        for idx in range(N):
            curr = nums[idx]
            
            if curr in _dict.keys():
                _dict[curr].append(idx) # O(1)
            if curr not in _dict.keys():
                _dict[curr] = [idx]
        
        
        for num, idx_list in _dict.items():
            # go through subsequent idx in idx_list
            list_len = len(idx_list)
            if list_len == 1:
                continue
            elif list_len > 1:
                for i in range(1, list_len):
                    if (idx_list[i] - idx_list[i-1]) <= k:
                        return True
        
        return False
