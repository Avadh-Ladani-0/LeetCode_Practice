class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums=sorted(nums)
        ans=[]
        dic={}

        for i,n in enumerate(sorted_nums):
            if n in dic:
                if sorted_nums[i]==sorted_nums[i]:
                    continue
            else:
                dic[n]=i

        for i in nums :
            ans.append(dic[i])

        return ans