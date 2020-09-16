class MinStack:

    def __init__(self):
        # This vector implemented as stack
        self.myMinstack = []
        # Since the stack can only pop the data in a certain order, 
        # !!!We dont actually need to sort the minimal element, we just need to record which is the smallest element at each stage!!!
        self.currentMins = [float(inf)] 


    def push(self, x: int) -> None:
        self.myMinstack.append(x)
        self.currentMins.append(min(x, self.currentMins[-1]))


    def pop(self) -> None:
        del self.currentMins[-1]
        del self.myMinstack[-1]
        

    def top(self) -> int:
        return self.myMinstack[-1]

    def getMin(self) -> int:
        return self.currentMins[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()