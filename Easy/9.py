class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        end = 0
        result = 0
        orig = x
        while x >0:
            end = x%10
            result = result*10 + end
            x = x/10
        if result ==orig:
            return True
        else:
            return False
            