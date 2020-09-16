# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Basically we use the list to do the sorting and rebuild the list
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None:
            return []
        #Converted into list and do the sorting
        converted = []
        while head != None:
            converted.append(head.val)
            head = head.next
        #print(converted)
        converted.sort()
        #Rebuild the list
        start = ListNode(converted[0])
        first = start
        for i in range(1, len(converted)):
            theNode = ListNode(converted[i])
            first.next = theNode
            first = first.next

        return start