class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        t1, t2 = 1, 2
        for i in range(3, n+1):
            curr = t2+t1
            t2,t1 = curr,t2

        return t2

        #n=4
        # cS(3) + 2*cS(2) - 1
        #3+4-1=7

        #1,1,1,1
        #1,1,2
        #1,2,1
        #2,1,1
        #2,2

        #2,2 -> [1,1,2], [2,2]
        #2,1,1 -> 
        #3,1

        #4->2,3->2+3->5
        #5->3,4->3+5->8
        #3,2->3
        #4,1->5