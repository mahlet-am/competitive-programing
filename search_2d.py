class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x=False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==target:
                    x=True
                    break
        return x 