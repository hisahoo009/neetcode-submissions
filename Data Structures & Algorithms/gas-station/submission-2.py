class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # gas = [1,2,3,4]
        # cost = [2,2,4,1]
        # diff = [-1,0,-1,3]
        # id 0: [-1,-1,-2,1]
        # id 1: [0,-1,2,1]
        # id 2: [-1,2,1,1]
        # id 3: [3,2,2,1]

        # gas: [1,2,3]
        # cost: [2,3,2]
        # diff: [-1,-1,1]

        N = len(gas)
        
        start_idx = 0
        current_tank = 0

        sumN = 0

        for i in range(N):
            num = (gas[i] - cost[i])
            sumN = sumN + num
            current_tank = current_tank +  num

            if current_tank < 0:
                current_tank = 0
                start_idx = i + 1
        
        if sumN >= 0:
            return start_idx
        
        return -1

        # gas=[5,8,2,8]
        # cost=[6,5,6,6]
        # diff = [-1,3,-4,2]
            