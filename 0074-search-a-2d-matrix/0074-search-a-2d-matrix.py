class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        found = 0
        while l <= r:
            mid = (l + r) // 2
            
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                found = mid
                break
            
            
        
        
        if not(l <= r):
            return False
        
        arr = matrix[mid]
        
        l, r = 0, len(arr) - 1
        
        
        while l <= r:
            mid = (l + r) // 2
            
            if arr[mid] > target:
                r = mid - 1
            elif arr[mid] < target:
                l = mid + 1
            else:
                return True
        
        
        return False
        