class Solution(object):
    def myAtoi(self, stri):
        """
        :type str: str
        :rtype: int
        """
        rawNum = stri.strip()
        num = rawNum
        inte = 0
        if rawNum == "":
            return 0
        sign = 1
        if rawNum[0] == "+":
            num = rawNum[1:]
            sign = 1
        elif rawNum[0] == "-":
            num = rawNum[1:]
            sign = -1
        for i in range(len(num)):
            if num[i] < '0' or num[i] >'9':
                break
            inte = inte*10 + int(num[i])
            if inte > (2**31-1):
                break
        inte *= sign
        if inte >= (2**31-1):
            return (2**31-1)
        elif inte <= (-2**31):
            return (-2**31)
        return inte