class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        counter={}

        for i in nums:
            if i not in counter:
                counter[i]=1
            else:
                if counter[i]==2:
                    counter[i]=1
                else:
                    counter[i]+=1

        for i in counter:
            if counter[i]%2!=0:
                return False
        
        return True