class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up, down = 0, len(matrix) - 1
        row = up + ((down - up) // 2)
        while up <= down:
            row = up + ((down - up) // 2)
            if matrix[row][0] < target:
                up = row + 1
            elif matrix[row][0] > target:
                down = row - 1
            else:
                return True
            
        if matrix[row][0] > target and row > 0:
            row -= 1

        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        return False