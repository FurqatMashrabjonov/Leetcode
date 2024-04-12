class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triples = []
        n = len(nums)
        for i in range(n):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            l, r = i + 1, n - 1
            
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    #equal
                    
                    triples.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # avoiding from duplicate triples
                    
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return triples