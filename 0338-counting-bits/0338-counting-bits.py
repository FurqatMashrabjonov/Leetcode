class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        cache = {}
        for num in range(n + 1):
            count = 0
            while num:
                if num in cache:
                    count += cache[num]
                    break
                    
                if num & 1 == 1:
                    count += 1
                
                num = num >> 1
            cache[num] = count
            res.append(count)
        
        return res