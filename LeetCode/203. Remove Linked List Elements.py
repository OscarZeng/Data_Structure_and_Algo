# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        #Easy Question with very tricky boundary conditions
        #As usual, we consider the None value, boundary value
        if head == None:
            return head
        dummy = ListNode(-1)
        #Since the very first node may be val to be removed.
        #We need to keep an eye on what is going on
        dummy.next = head
        #Here only the dummy head we created will last for sure.
        #Hence we should keep stucking on the dummy
        start = dummy
        while dummy.next != None:
            if dummy.next.val == val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next 
        #As we know we should return base on the for sure point
        return start.next
            