class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        pi=0
        ni=1
        for i in nums:
            if i>0:
                ans[pi]=i
                pi+=2
            if i<0:
                ans[ni]=i
                ni+=2
        return ans


            


            
