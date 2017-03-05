class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k>0 and len(nums)>1:
            nums[:] = nums[len(nums) - k:] +nums[:len(nums)-k]