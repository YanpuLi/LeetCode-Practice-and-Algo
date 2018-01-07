'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        elif x < 0:
            flag =-1
            x = x*(-1)
        else:
            flag = 1
        result = 0 
        while x > 0:
            result = result*10 +x%10
            x = x/10
        if result < -(1 << 31) or result > (1 << 31) - 1:
            return 0
            
        else:
            return result*flag