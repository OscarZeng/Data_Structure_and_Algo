# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#When modify the linked list nodes, always remember to break the linked list when moving the node
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        #Since we can regard the first node as already sorted
        #The node that is currently being checked
        lastSorted = head
        while lastSorted.next != None:
            toBeChecked = lastSorted.next
            print("lastSorted", lastSorted.val)
            print("toBechecked", toBeChecked.val)
            #If it is the biggest value, simple move the index of lastSorted
            if toBeChecked.val >= lastSorted.val:
                lastSorted = lastSorted.next
                continue
            #Always remember to Break the chain
            lastSorted.next = toBeChecked.next
            #check if is the smallest
            
            if toBeChecked.val <= head.val:
                toBeChecked.next = head
                head = toBeChecked
            #not the smallest
            else:
                pointer = head
                while pointer != lastSorted and toBeChecked.val > pointer.next.val:
                    pointer = pointer.next
                toBeChecked.next = pointer.next
                pointer.next = toBeChecked
                # if pointer == lastSorted:
                #     lastSorted = toBeChecked
            
        return head
        