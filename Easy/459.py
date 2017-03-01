# divide string into half, to see if meets requirements, otherwise into one/third....
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <2: return False
        pos = len(s)/2
        while pos >0:
            if len(s) % pos ==0:
                sub = s[:pos]
                num = len(s)/pos
                if sub*num == s:
                    return True
            pos -=1
        return False
# regular expression
def repeatedSubstringPattern(self, str):

    import re
    return bool(re.match(r"^([a-z]+)\1+$", str))
# s+s, and removing first and last letter in s+s, to see if a s in s+s[1:-1]
def repeatedSubstringPattern(self, str):

        """
        :type str: str
        :rtype: bool
        """
        if not str:
            return False

        ss = (str + str)[1:-1]
        return ss.find(str) != -1