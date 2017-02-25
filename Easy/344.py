class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = list(s)
        i,j = 0, len(string)-1
        while i<j:
            temp = string[i]
            string[i] = string[j]
            string[j] =temp
            i += 1
            j -= 1
        
        return ''.join(string)
class Solution2(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]