class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index=0
        count=0

        for i in range(len(nums)):
            if nums[i]!=val:
                nums[index]=nums[i]
                index+=1
                print(nums)
                count+=1
        
        return count