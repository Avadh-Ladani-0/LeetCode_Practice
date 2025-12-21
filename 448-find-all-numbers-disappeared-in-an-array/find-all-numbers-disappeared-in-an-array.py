class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr=[0]*(len(nums)+1)
        ans=[]
        for i in range(len(nums)):
            arr[nums[i]]=arr[nums[i]]+1

        for i in range(1,len(arr)):
            if arr[i]==0:
                ans.append(i)

        return ans