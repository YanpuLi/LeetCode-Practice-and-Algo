class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) ==1:
            return True
            
        # count num of Capitals, count1 num of lowercases    
        count = 0
        count1 = 0
        for i in xrange(len(word)):
            if ord(word[i]) <=90:
                count += 1
            else:
                count1 +=1
                
        if count == len(word) or count1 == len(word):
            return True
        if count >1:
            return False
        if count ==1 and ord(word[0]) <=90:
            return True
        return False