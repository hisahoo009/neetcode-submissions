class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # transpose matrix
        # [1 2 3]    [1 4 7]
        # [4 5 6] -> [2 5 8]
        # [7 8 9]    [3 6 9]

        n = len(matrix) # 2

        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

            #print(matrix)        

            left, right = 0, n-1
            while (left < right):
                matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
                left, right = left + 1, right - 1 
