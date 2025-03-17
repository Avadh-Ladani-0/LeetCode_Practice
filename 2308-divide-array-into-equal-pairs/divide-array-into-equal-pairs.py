class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        counter={}

        for i in nums:
            if i not in counter:
                counter[i]=1
            else:
                counter[i]+=1

        for i in counter:
            if counter[i]%2==1:
                return False
        
        return True