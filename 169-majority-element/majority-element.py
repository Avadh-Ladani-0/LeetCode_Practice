class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        cnt = 1 
        el = nums[0] 

        for i in range(1,n):
            if cnt == 0:
                el = nums[i]
                cnt += 1
            elif el == nums[i]:
                cnt += 1
            else:
                cnt -= 1

        # cnt1 = 0
        # for i in range(n):
        #     if nums[i] == el:
        #         cnt1 += 1

        # if cnt1 > (n / 2):
        #     return el
        return el
        