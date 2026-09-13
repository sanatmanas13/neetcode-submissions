class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp={}
        for i in nums:
            if i not in mp:
                mp[i] = 0
            mp[i] += 1
        buck=[[] for _ in range(len(nums)+1)]
        for i in mp:
            freq=mp[i]
            buck[freq].append(i)

        result=[]
        for freq in range(len(nums),0,-1):
            for i in buck[freq]:
                result.append(i)

                if len(result)==k:
                    return result
