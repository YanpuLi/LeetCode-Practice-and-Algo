class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        listNum = list(str(num))
        stop = False
        while not stop:
            listNum =map(int, listNum)
            add = sum(listNum)
            listNum = list(str(add))
            if len(listNum) ==1:
                stop = True
        return int(listNum[0])
class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        return (num - 1) % 9 + 1 if num > 0 else 0