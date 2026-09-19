class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        temp=-1
        for i in range(len(nums)):
            if nums[i]==0:
                if temp==-1:
                    temp=i
                else:
                    return [0]*len(nums)
            else:
                prod*=nums[i]
        ans=[]
        if temp==-1:
            for i in nums:
                ans.append(prod//i)
        else:
            for i in range(len(nums)):
                if i==temp:
                    ans.append(prod)
                else:
                    ans.append(0)
        return ans
        
            