# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Own solution by convert it into list and rebuild a linkedlist
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return None
        start = head
        convertedList = []
        while head != None:
            convertedList.append(head.val)
            head = head.next
        head = start
        convertedList.pop(0)
        #print(convertedList, head.val)
        isFront = False

        while len(convertedList) != 0:
            if isFront == False:
                currValue = convertedList.pop()
            else:
                currValue = convertedList.pop(0)
            isFront = not isFront
            newNode = ListNode(currValue)
            head.next = newNode
            head = head.next

        return start
