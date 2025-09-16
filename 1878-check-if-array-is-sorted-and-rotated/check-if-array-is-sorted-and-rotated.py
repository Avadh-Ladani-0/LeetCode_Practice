class Solution:
    def check(self, nums: List[int]) -> bool:
        breaks=0
        n=len(nums)
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                breaks+=1
        if breaks<=1:
            return True
        else:
            return False