class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        prefix_sum=0
        d={0:1}

        for i in nums:
            prefix_sum+=i
            if prefix_sum-k in d :
                count+=d[prefix_sum - k]
            if prefix_sum in d:
                d[prefix_sum]+=1
            else:
                d[prefix_sum]=1
        
        return count

    # __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
        