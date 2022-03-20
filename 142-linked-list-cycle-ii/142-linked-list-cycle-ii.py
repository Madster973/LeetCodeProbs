# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Code to detect the cycle in Linked List
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
        except Exception:
            return None
        # If the cycle ends at n we always converge at n-1 so we need to do slow/
        # fast to next
        fast = fast.next
        # Increment slow/fast or head till they meet. They meet only at the starting of the 
        # Loop
        while head is not fast:
            head = head.next
            fast = fast.next
        return head
        
        