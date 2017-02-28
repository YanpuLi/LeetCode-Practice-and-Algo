class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        using one_step, two_step to find the second half, and reverse it, then compare
        """
        if not head or not head.next: return True
        one_step = head
        two_step = head
        while two_step.next and two_step.next.next:
            one_step = one_step.next
            two_step = two_step.next.next
        #reverse the second half
        left = head
        right = self.reverse(one_step.next)
        while right:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        return True
    def reverse(self, head):
        p = head.next
        head.next = None
        while p:
            next, p.next = p.next, head
            head, p = p, next
        return head
        
    def isPalindrome2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l1 = []
        while head:
            l1.append(head.val)
            head = head.next
        return l1 == l1[::-1]