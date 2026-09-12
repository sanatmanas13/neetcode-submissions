class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            temp = ''.join(sorted(s))
            if temp not in mp:
                mp[temp] = []
            mp[temp].append(s)
        return list(mp.values()) 
        