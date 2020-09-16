# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        #Firstly check whether the linked list has at least two nodes,
        #In which case directly accessing the linked list may result in error
        if head == None or head.next == None:
            return head
        p1, p2= head, head.next
        #As usual, we need to keep the head node.
        #Take notice that the first node may be different given this condition
        start = p1.next
        while 1:
            p1.next = p2.next
            p2.next = p1
            #Check the odd number length
            if p1.next == None or p1.next.next == None:
                return start 

            #Here the point is to make the pointer points to the right node
            #when the switching node is done
            p2 = p1.next    
            p1.next = p1.next.next
            #Move to the next pair
            p1 = p2
            p2 = p1.next
            
        return start