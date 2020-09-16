# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
    	#Use a set to record all the visited nodes
        visited = set()
        while head != None:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        
        return None