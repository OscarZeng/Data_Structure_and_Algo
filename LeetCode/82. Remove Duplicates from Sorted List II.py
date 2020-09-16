# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Own solution by keep removing the front same nodes, which is very troublesome
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next ==None:
            return head
        #In case we have the situation like [1,1,1,2,2,2]
        #We must make sure that the first two nodes have different values
        while head.val == head.next.val:
            #Here we remove the all the same nodes in the front
            while head.val == head.next.val:
                #remove all the same value nodes in the front
                head = head.next
                #Check whether all the nodes are the same
                if head.next == None:
                    return None
            head = head.next
            #After remove front, we have the new linkedlist, which means we should do everthing again
            if head == None or head.next ==None:
                return head
                
        start = head
        first = head
        second = head.next
        while second.next != None:
            if second.val == second.next.val:
                while second.val == second.next.val:
                    second = second.next
                    if second.next == None:
                        first.next = None
                        return start
                second = second.next
                first.next = second
            else:
                first = first.next
                second = second.next
        
        return start



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Own solution which manually adding a dummy node at the front can solve the problem easily
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next ==None:
            return head
        dummy = ListNode("a")
        dummy.next = head
        start = dummy
        first = dummy
        second = head
        while second.next != None:
            if second.val == second.next.val:
                while second.val == second.next.val:
                    second = second.next
                    if second.next == None:
                        first.next = None
                        return start.next
                second = second.next
                first.next = second
            else:
                first = first.next
                second = second.next
        
        return start.next


        