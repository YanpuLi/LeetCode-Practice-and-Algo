class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        l = len(p)
        occ = []
        dicp ={}
        for k in p:
            dicp[k] = dicp.get(k,0)+1
        for i in xrange(len(s)-l+1):
            dicj = {}
            for j in s[i:i+l]:
                dicj[j] = dicj.get(j,0)+1
            if dicp == dicj:
                occ.append(i)
        return occ
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ls, lp = len(s), len(p)
        count = lp
        cp = collections.Counter(p)
        ans = []
        for i in range(ls):
            if cp[s[i]] >=1 :
                count -= 1
            cp[s[i]] -= 1
            if i >= lp:
                if cp[s[i - lp]] >= 0:
                    count += 1
                cp[s[i - lp]] += 1
            if count == 0:
                ans.append(i - lp + 1)
        return ans