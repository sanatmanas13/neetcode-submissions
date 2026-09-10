class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        n = len(nums)
        for x in nums: 
            if x in freq:
                return True
            freq[x] = 1
        return False;