class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        pairs = {}
        for idx, val in enumerate(nums):
            if val not in pairs.values():
                pairs[idx] = target - val # target - val = complement num
                continue
            
            if val in pairs.values():
                keys = [k for k, v in pairs.items() if v == val]
                res = [keys[0], idx]
                break
        
        return res