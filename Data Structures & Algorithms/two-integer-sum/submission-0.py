class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        indx = 0
        for i in nums:
            need = target - i
            if need not in seen:
                seen[i] = indx
                indx += 1
            else:
                return [seen.get(need), indx] 


        