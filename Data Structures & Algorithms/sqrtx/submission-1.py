class Solution:
    def mySqrt(self, x: int) -> int:
        
        # Make a guess (z)
        z = x / 2
        
        while abs(z ** 2 - x) > 0.0001:
            # New Guess, y = 0.5 * (z + N/z)
            y = 0.5 * (z + (x / z))    
            z = y if (y != 0) else e-10 
        
        return math.floor(z)