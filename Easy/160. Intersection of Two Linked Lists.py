'''
find the point where ListA, B have the same length
'''

class Solution(object):
    def getLength(self, head):
        node = head
        count = 0
        while node:
            count +=1
            node =node.next
        return count
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lA = self.getLength(headA)
        lB = self.getLength(headB)
        for i in xrange(0, lA-lB):
            headA = headA.next
        for i in xrange(0, lB-lA):
            headB = headB.next
        while headA!=headB:
            headA = headA.next
            headB = headB.next
        return headA