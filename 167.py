class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums)-1
        while i < j:
            result = nums[i] +nums[j]
            if result > target:
                j = j-1
            elif result < target:
                i = i+1
            else:
                return (i+1,j+1)