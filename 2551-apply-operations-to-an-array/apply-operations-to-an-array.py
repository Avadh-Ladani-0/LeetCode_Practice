class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i=0
        while i<=len(nums)-2:
            if nums[i]==nums[i+1]:
                nums[i]=2*nums[i]
                nums[i+1]=0
                i+=2
            else:
                i+=1
        index=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[index]=nums[index],nums[i]
                index+=1
        return nums