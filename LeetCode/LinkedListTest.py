class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
	def checkNode(self):
		print("self.val:",self.val)
		print("self.next",self.next.val if self.next != None else "None")

a = ListNode("a")
b = ListNode("b")
c = ListNode("c")
a.next = b
b.next = c
a.checkNode()
b.checkNode()
c.checkNode()
q = a
q.val = "q"
a.checkNode()
b.checkNode()
c.checkNode()
q.checkNode()
		

