class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        stack = []
        sum = 0
        for item in nestedList:
            stack.append((item, 1))
        while stack:
            num, d = stack.pop()
            if num.isInteger():
                sum += num.getInteger()*d
            else:
                for j in num.getList():
                    stack.append((j, d+1))
        return sum