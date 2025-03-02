class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        left=0
        right=0
        res=[]

        while left<len(nums1) and right<len(nums2):
            if nums1[left][0]==nums2[right][0]:
                temp=[]
                temp.append(nums1[left][0])
                temp.append(nums1[left][1]+nums2[right][1])
                res.append(temp)
                left+=1
                right+=1
            else:
                if nums1[left][0] < nums2[right][0]:
                    res.append(nums1[left])
                    left+=1
                else:
                    res.append(nums2[right])
                    right+=1
            
        while left<len(nums1):
            res.append(nums1[left])
            left+=1
        
        while right<len(nums2):
            res.append(nums2[right])
            right+=1

        # res.extend(nums1[left:])
        # res.extend(nums2[right:])

        return res

