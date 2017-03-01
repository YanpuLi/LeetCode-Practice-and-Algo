class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        pos = []
        letter = []
        vowels = 'aeiouAEIOU'
        for i in xrange(len(s)):
            if s[i] in vowels and s[i] not in letter:
                pos.append(i)
        listS = list(s)
        print pos
        i,j = 0, len(pos)-1
        while i<j:
            listS[pos[i]],listS[pos[j]] = listS[pos[j]], listS[pos[i]]
            i +=1
            j -=1
        return ''.join(listS)