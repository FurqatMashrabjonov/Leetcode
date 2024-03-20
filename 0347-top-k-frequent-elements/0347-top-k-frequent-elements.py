class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            list[n] = 1 + list.get(n, 0)
        
        for n, c in list.items():
            freq[c].append(n)
        res = []
        for n in range(len(freq) - 1, 0, -1):
            for i in range(len(freq[n])):
                res.append(freq[n][i])
                if len(res) == k:
                    return res