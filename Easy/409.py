class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        'ccc'
        """
        dic = {}
        for i in xrange(len(s)):
            dic[s[i]] = dic.get(s[i], 0) +1
        count = 0
        odd = False
        for item in dic.values():
            if item%2 ==0:
                count +=item
            else:
                count += item-1
                odd = True
        if odd:
            return count+1
        return count