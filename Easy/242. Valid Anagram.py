class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        import collections
        dic = collections.Counter(s)
        dic1 = collections.Counter(t)
        if dic == dic1:
            return True
        return False