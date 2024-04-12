class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        obj = {}
        res = []
        for i in range(len(nums)):
            obj[nums[i]] = 1 + obj.get(nums[i], 0)
        
        freq = [[] for i in range(len(nums) + 1)]
        
        for key, v in obj.items():
            freq[v].append(key)
    
        for i in range(len(freq) - 1, 0, -1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) == k:
                    return res
        