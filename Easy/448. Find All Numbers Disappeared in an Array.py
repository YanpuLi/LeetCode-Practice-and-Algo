class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num = set(nums)
        range = []
        for i in xrange(len(nums)):
            range.append(i+1)
        return list(set(range) - num)