class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None: return None
        new_head = ListNode(0)
        curr = head
        prev = new_head
        prev.next = head
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = prev
            prev = curr
            curr = curr.next
        return new_head.next