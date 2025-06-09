class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        index=0
        for i in nums:
            if i>0:
                ans[index]=i
                index+=2
        index=1
        for i in nums:
            if i<0:
                ans[index]=i
                index+=2
        return ans


            


            
