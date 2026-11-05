class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        L, R = 0, rows * cols - 1
        
        while L <= R:
            mid = (L + R) // 2
            row, col = mid // cols, mid % cols
            if target < matrix[row][col]:
                R = mid - 1
            elif target > matrix[row][col]:
                L = mid + 1
            else:
                return True
        return False