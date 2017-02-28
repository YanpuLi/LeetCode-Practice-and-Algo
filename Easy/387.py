
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in xrange(len(s)):
            if dic.get(s[i])==None: 
                dic[s[i]] = [i]
            else:
                dic[s[i]].append(i)
        # store the index in a list, then find min
        result = [dic[i][0] for i in dic if len(dic[i]) ==1]
        if len(result) != 0:
            return min(result)
        return -1
'''
using collections
'''
    def firstUniqChar2(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = collections.Counter(s)
        for i, c in enumerate(s):
            if x[c] == 1:
                return i
        return -1
