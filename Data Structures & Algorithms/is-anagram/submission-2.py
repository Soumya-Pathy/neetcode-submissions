class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        seen1 = {}
        if len(s) != len(t):
            return False
        for i in s:
            seen[i] = seen.get(i, 0) + 1 
        for i in t:
            if i not in seen:
                return False
            seen1[i] = seen1.get(i, 0) + 1
        
        return seen == seen1
