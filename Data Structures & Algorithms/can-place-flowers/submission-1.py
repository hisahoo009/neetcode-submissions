class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        # 0 0 0 1 = floor(num(0)/2)
        # 1 0 0 0 
        # 1 0 0 0 1 = if num(0) is odd then floor(num(0)/2) else (num(0)/2 - 1)

        N = len(flowerbed) # N = 5
        one_indices = [i for i, val in enumerate(flowerbed) if val==1] # [0,4]

        placed = 0
        if not one_indices:
            placed = math.ceil(N/2)

        if one_indices: 
            placed = math.floor(one_indices[0]/2) # 0

            for i, idx in enumerate(one_indices[:-1]):
                curr = idx
                next = one_indices[i+1]

                num_zeros = next - curr - 1
                if num_zeros % 2 == 1:
                    placed = placed + math.floor(num_zeros/2) # placed = 1
                if num_zeros % 2 == 0:
                    placed = placed + (num_zeros/2) - 1
            

            placed = placed + math.floor((N - one_indices[-1] - 1)/2)

        if n <= placed:
            return True

        return False

