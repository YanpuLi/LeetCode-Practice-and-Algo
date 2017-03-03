class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t): return False
        dicS = {}
        for i in xrange(len(s)):
            if s[i] not in dicS:
                dicS[s[i]] = [i]
            else:
                dicS[s[i]].append(i)
        dicT = {}
        for j in xrange(len(t)):
            if t[j] not in dicT:
                dicT[t[j]] = [j]
            else:
                dicT[t[j]].append(j)
        if len(dicS.values()) == len(dicT.values()):
            if len(filter(lambda x: x not in dicT.values(), dicS.values())) == 0:
                return True
        return False