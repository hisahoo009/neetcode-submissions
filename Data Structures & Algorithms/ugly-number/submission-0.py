class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n <= 0:
            return False
        if n == 1:
            return True

        # 11 -> False
        # 6 -> 3
        if n >= 2:
            prime_numbers = [2, 3, 5]
            while (n != 1):
                div = False
                for prime in prime_numbers:
                    if n % prime == 0:
                        n = n // prime
                        div = True
                        break
                if div == False:
                    return False
        
            if n == 1:
                return True
        
        return False
