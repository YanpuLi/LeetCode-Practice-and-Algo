'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''
import time
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        t1 = time.time()
        for i in xrange(len(haystack) - len(needle) + 1):
            if haystack[i:len(needle)+i] == needle:
                print "Method1: costing %f s"%(time.time()-t1)
                return i
        print "Method1: costing %f s"%(time.time()-t1)
        return -1
    def strStr2(self, haystack, needle):
        t1 = time.time()
        if len(needle) > len(haystack):
            print "Method2: costing %f s"%(time.time()-t1)
            return -1
        if len(needle) == 0:
            print "Method2: costing %f s"%(time.time()-t1)
            return 0
        for i in xrange(len(haystack)):
            for j in xrange(len(needle)):
                if i+j == len(haystack):
                    print "Method2: costing %f s"%(time.time()-t1)
                    return -1
                if haystack[i+j] != needle[j]:
                    if i+j == len(haystack)-1:
                        print "Method2: costing %f s"%(time.time()-t1)
                        return -1
                    break
                else:
                    if j == len(needle)-1:
                        print "Method2: costing %f s"%(time.time()-t1)
                        return i
            
            
                
obj = Solution()
obj.strStr("mississippi","abbbbb")
obj.strStr2("mississippi","abbbbb")