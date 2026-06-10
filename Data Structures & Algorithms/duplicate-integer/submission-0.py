class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = []
        for i in nums:
            if i in new:
                return True
            else:
                new.append(i)
        return False