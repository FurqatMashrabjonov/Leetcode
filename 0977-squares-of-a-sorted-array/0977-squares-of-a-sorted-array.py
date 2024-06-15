class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j, n = 0, len(nums) - 1, len(nums)
        res = [0 for _ in range(n)]
        pos = n - 1
        while pos >= 0:
            if abs(nums[i]) < abs(nums[j]):
                res[pos] = nums[j] ** 2
                j -= 1
            else:
                res[pos] = nums[i] ** 2
                i += 1
                
            pos -= 1
        
        return res