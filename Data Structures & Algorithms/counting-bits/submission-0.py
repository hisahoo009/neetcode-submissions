class Solution:
    def countBits(self, n: int) -> List[int]:
    
        # 1 -> 001 -> 1
        # 2 -> 010 -> 1
        # 3 -> 011 -> 2
        # 4 -> 100 -> 1
        # 5 -> 101 -> 2
        # 6 -> 110 -> 2
        # 7 -> 111 -> 3
        # 8 -> 1000 -> 1
        # 9 -> 1001 -> 2
        # 10 -> 1010 -> 2
        # 11 -> 1011 -> 3
        # 12 -> 1100 -> 2
        # 13 -> 1101 -> 3
        # 14 -> 1110 -> 3
        # 15 -> 1111 -> 4
        # 16 -> 10000 -> 5
        
        # 5 -> 2 -> 1
        res = [0]
        
        for num in range(1, n+1):
           binary = f"{num:b}"
           count = sum([int(ch) for ch in binary if ch=='1'])
           res.append(count)
        
        return res