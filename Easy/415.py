class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l3 = []
        add = 0
        digit = 0
        i,j = len(num1), len(num2)
        while i or j or add:
            digit = add
            if i:
                i -=1
                digit += int(num1[i])
            if j:
                j -=1
                digit += int(num2[j])
            add = digit >9
        
            l3.append(str(digit%10))
        return ''.join(l3[::-1])