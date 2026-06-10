class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            seen[i] = seen.get(i,0)+1
        sort_seen = dict(sorted(seen.items(), key=lambda item: item[1], reverse = True))
        t = k
        result = []
        for i in sort_seen:
            if t > 0:
                result.append(i)
                t -= 1
        return result
            
