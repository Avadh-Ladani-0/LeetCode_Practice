class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        freq={}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product=nums[i]*nums[j]
                if product not in freq:
                    freq[product]=1
                else:
                    freq[product]+=1
        cnt=0
        for i in freq:
            val=freq[i]
            if val>=2:
                cnt+=(val*(val-1))//2

        return cnt*8