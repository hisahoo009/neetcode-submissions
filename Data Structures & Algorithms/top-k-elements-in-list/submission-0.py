class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create dict
        _dict = {}
        res = []
        N = len(nums) # 6

        # traverse array: O(N)
        for num in nums: # _dict = {1:1, 2:2, 3:3}
            #   if key does not exist, create_key -> val: 1
            _dict[num] = (_dict[num] + 1) if num in _dict.keys() else 1
        
        # sort dict values in descending order: O(NlogN)
        # [3,2,1]
        dict_values = sorted(_dict.values(), reverse=True)

        # traverse values: O(N)
        count = 0
        for val in dict_values:
            top_keys = [k for k, v in _dict.items() if v == val]
            # res.append(key)
            res.append(top_keys[0])
            # del _dict[key]
            del _dict[top_keys[0]]
            
            count = count + 1
            if count == k:
                break
        
        return res
        