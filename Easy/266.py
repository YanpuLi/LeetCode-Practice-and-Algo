class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        record the occurance of each character: num
        only 1 or no odd num is allowed
        """
        dic = {}
        '''for i in xrange(len(s)):
            if s[i] not in dic.keys():
                dic[s[i]] = 1
            else:
                dic[s[i]] +=1'''
        for i in xrange(len(s)):
            dic[s[i]] = dic.get(s[i], 0) +1
        count = 0
        for item in dic.values():
            if item%2 == 1:
                count +=1
                
        if count >1:
            return False
        return True