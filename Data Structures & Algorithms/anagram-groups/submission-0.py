class Solution:
    def anagrams(self, s,t):
        if len(s) != len(t):
            return False

        seen = {}
        for a,b in zip(s,t):
            seen[a] = seen.get(a,0) + 1
            seen[b] = seen.get(b,0) - 1

        return all(v == 0 for v in seen.values())
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        while len(strs) > 0:
            new = []
            s = strs[0]
            new.append(s)
            indx = []
            for i in range(len(strs)-1):
                if self.anagrams(s,strs[i+1]):
                    new.append(strs[i+1])
                    indx.append(i+1)
            
            for j in sorted(indx, reverse=True):
                strs.pop(j)
            strs.pop(0)
            result.append(new)
        return result