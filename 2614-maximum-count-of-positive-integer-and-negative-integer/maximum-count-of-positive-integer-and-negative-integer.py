class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg_count=0
        pos_count=0

        for i in nums:
            if i<0:
                neg_count+=1
            elif i>0:
                pos_count+=1
        
        return max(neg_count,pos_count)