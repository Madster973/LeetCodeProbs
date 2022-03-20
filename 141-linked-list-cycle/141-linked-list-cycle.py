# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Initialise the slow to head and fast one step ahead
        slow= fast = head
        # Run the loop till fast reaches the end of the loop
        while fast and fast.next:
            # Increment the slow by 1 step and fast by 2 steps
            slow = slow.next
            fast = fast.next.next
            # Check if slow is equal to fast or not and return True
            if slow == fast:
                return True
        # If fast has reached the end point and slow and fast are not equal then return False
        return False

    



        