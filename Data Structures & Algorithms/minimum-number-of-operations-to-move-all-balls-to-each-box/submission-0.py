class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        answer, N = [], len(boxes)

        # ans[i] = boxes[j] * abs(j-i)
        one_indices = [idx for idx, val in enumerate(boxes) if (val == '1')]
        
        for i in range(N):
            ans = 0
            for idx in one_indices:
                ans = ans + abs(idx - i)
            
            answer.append(ans)

        return answer
