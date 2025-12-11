class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr=[0]*(len(nums)+1)
        miss=0
        dup=0

        for i in range(len(nums)):
            arr[nums[i]]+=1

        for i in range(len(arr)):
            if arr[i]==2:
                dup=i
            elif arr[i]==0:
                miss=i
        
        return [dup,miss]