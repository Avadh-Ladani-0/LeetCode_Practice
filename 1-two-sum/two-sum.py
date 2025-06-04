class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2=sorted(nums)
        i=0
        j=len(nums)-1
        while i < j:
            pairsum=nums2[i]+nums2[j]

            if pairsum<target:
                i+=1
            elif pairsum>target:
                j-=1
            else:
                break

        ans=[]

        for x in range(len(nums)):
            if nums2[i]==nums[x] or nums2[j]==nums[x]:
                ans.append(x)
        return ans

