class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        for i in range(len(nums)):
            rem=target-nums[i]
            if rem in m:
                return [m[rem],i]
            m[nums[i]]=i
        return [-1,-1]