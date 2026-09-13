class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        pp = 1
        for i in nums:
            ans.append(pp)
            pp *= i
        pp=1
        for i in range(len(ans)-1,-1,-1):
            ans[i] *= pp
            pp *= nums[i]
        return ans