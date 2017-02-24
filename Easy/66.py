class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        stop = False
        newdigits = []
        digits[-1] = digits[-1]+1
        i = len(digits)-1
        while i>0 and not stop:
            if digits[i]>9:
                digits[i] = digits[i] - 10
                digits[i-1] = digits[i-1]+1
            else:
                stop = True
            i = i-1
        if digits[0]>9:
            digits[0] = digits[0] -10
            newdigits.append(1)
        newdigits = newdigits + digits
        return newdigits
            