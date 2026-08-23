class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        n = len(grid)
        
        total = pow(n,2) * (pow(n,2) + 1)
        total = total // 2

        all_items = set()
        sum_all = 0 # total + a - b 
        for row in range(n):
            all_items.update(grid[row])
            sum_all += sum(grid[row])
        
        # total - b
        sum_distinct = sum(list(all_items))
        a = sum_all - sum_distinct

        #total + a - b = sum_all
        b = total + a - sum_all

        return [a,b]