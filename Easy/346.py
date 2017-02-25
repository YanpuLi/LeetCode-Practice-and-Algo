class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.items = []
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        avg = 0
        self.items.append(val)
        length = len(self.items)
        if length <= self.size:
            
            avg = float(sum(self.items))/length
        else:
            self.items = self.items[1:]
            avg = float(sum(self.items))/self.size
        return avg