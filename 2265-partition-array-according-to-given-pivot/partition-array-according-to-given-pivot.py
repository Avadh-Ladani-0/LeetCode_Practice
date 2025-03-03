class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left=[]
        right=[]

        for i in range(len(nums)):
            if nums[i]<pivot:
                left.append(nums[i])
            elif nums[i]>pivot:
                right.append(nums[i])

        return left+[pivot]*(len(nums)-(len(left)+len(right)))+right