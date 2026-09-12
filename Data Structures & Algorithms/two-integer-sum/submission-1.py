class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        c=0
        for i in nums:
            if target-i in mp:
                return [mp[target-i],c] 
            mp[i] = c;
            c += 1
        return []