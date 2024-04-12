class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqSet = set(nums)
        maxlen = 0
        for num in nums:
            if num - 1 not in seqSet:
                length = 0
                while num + length in seqSet:
                    length += 1
                maxlen = max(maxlen, length)
                
        return maxlen