class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums2) > len(nums1): 
            nums1,nums2 = nums2, nums1
        dic1 = {}
        ans = []
        for i in nums1:
            dic1[i] = dic1.get(i,0)+1
        for j in nums2:
            if j in dic1 and dic1[j] >0:
                ans.append(j)
                dic1[j] -=1
        return ans
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        i,j = 0,0
        ans = []
        while i <len(nums1) and j<len(nums2):
            if nums1[i] < nums2[j]:
                i +=1
            elif nums1[i] > nums2[j]:
                j +=1
            else:
                ans.append(nums1[i])
                i +=1
                j +=1
        return ans