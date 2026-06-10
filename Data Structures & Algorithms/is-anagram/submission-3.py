class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        if len(s) != len(t):
            return False

        for a,b in zip(s,t):
            seen[a] = seen.get(a,0) + 1
            seen[b] = seen.get(b,0) - 1

        return all(v == 0 for v in seen.values())