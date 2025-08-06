class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res=0
        pre_sum=0

        for i in range(len(nums)):
            pre_sum+=nums[i]
            res=max(res,((pre_sum+i)//(i+1)))
        return res