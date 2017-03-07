class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: return head
        front = head
        mid = None
        last = None
        while front.next!= None:
            mid = front
            front = front.next
            mid.next = last
            last = mid
        front.next = mid
        return front
    def reverseList(self, head):
        curt = None
        while head !=None:
            temp = head.next
            head.next = curt
            curt = head
            head = temp
        return curt
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: return head
        last = head.next
        result = self.reverseList(last)
        head.next = None
        last.next = head
        return result
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        return self._reverse(head)
        
    def _reverse(self, node, prev = None):
        if not node:
            return prev
        
        n = node.next
        node.next = prev
        prev = node
        return self._reverse(n, node)
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: return head
        last = head.next
        result = self.reverseList(last)
        head.next = None
        last.next = head
        return result