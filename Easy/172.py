class Solution(object):
    def trailingZeroes(self,n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        count=0
        while n:
            n = n//5
            count += n
        return count

'''
calculate factorial
'''

def fact(n):
    if n <= 1: return 1
    else:
        return fact(n-1)*n