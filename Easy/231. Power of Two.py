class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #the binary format of n should be 10*
        count1 = 0
        while n >0:
            if n%2!=0:
                count1 +=1
            n = n/2
        if count1 ==1:
            return True
        return False
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n > 0 and n & (n - 1) == 0
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import re
        if re.match(r'^1[0]+|1',str(binaryN)):
            return True
        return False