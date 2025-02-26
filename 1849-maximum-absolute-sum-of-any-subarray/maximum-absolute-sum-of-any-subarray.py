class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        currsum=0
        maxsum=float('-inf')
        for i in nums:
            currsum=max(0,currsum+i)
            maxsum=max(maxsum,currsum)
            
        minsum=float('inf')
        currsum=0
        for j in nums:
            currsum=min(0,currsum+j)
            minsum=min(minsum,currsum)
            
        
        return max(maxsum,abs(minsum))