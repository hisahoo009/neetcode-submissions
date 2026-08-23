class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    # [1,2,3,3]
    def add(self, val: int) -> int:
        
        N = len(self.nums)
        if N == 0:
            self.nums.append(val)
            
        if val >= max(self.nums):
            self.nums.insert(N, val)
        
        if val < max(self.nums):
            for i in range(N):
                if self.nums[i] >= val:
                    self.nums.insert(i, val)
                    break
        #print(self.nums)
        return self.nums[-self.k]
        
        
