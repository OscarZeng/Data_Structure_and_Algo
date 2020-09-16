# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        start = head
        while head.next != None:
            #Check whether the next value equals to the next one, if equals, remove it
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        
        return start