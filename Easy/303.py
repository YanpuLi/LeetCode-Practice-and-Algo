'''
array is immutable

when doing init, directly doing sum, and put in a list
'''
class NumArray(object):
    def __init__(self, nums):
        self.dp = []
        self.acc = 0
        for i in xrange(len(nums)):
            self.acc = self.acc+ nums[i]
            self.dp.append(self.acc)

    def sumRange(self, i, j):
        return self.dp[j] - (self.dp[i-1] if i > 0 else 0)