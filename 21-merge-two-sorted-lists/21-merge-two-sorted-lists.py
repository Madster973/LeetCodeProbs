# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #  # Maintain dummy node to get the structure of New from starting
        # # We won't be able to return the New node as we are incrementing it
        # dummy = New = ListNode(0)
        # # Running till one of the list is exhausted
        # while list1 and list2:
        #     # Compare the list1 and list2 values and assign the next to the list which has less
        #     # value. Increment the assigned list and the new list
        #     if list1.val <= list2.val:
        #         New.next = list1
        #         list1=list1.next
        #         New = New.next
        #     else:
        #         New.next = list2
        #         list2=list2.next
        #         New = New.next
        # # As one of the list is exhausted, you need to assign the next of new to the list
        # # which has elements left (none or element = element)
        # New.next = list1 or list2
        # return dummy.next
        
        
        # Recursive way of approach for Merge Sort
        # Check if any of the list is empty then return the list which is non empty
        if not list1 or not list2:
            return list1 or list2
        # If list1's value is less then we need to perform mergesort on list1.next and list2
        if list1.val<=list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        # If list2's value is less then we need to perform mergesort on list2.next and list1
        else:
            list2.next = self.mergeTwoLists(list2.next,list1)
            return list2
        
       
        