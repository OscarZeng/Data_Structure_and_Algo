class Solution:
    def __init__(self):
    	pass
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
        	#Here the (x & y) will be the carrier
        	#When two adders are the 1 at certian position, there will be carrier
        	#Afterwards, we keep adding the carrier to the ans until there is no carrier
            x, y = x ^ y, (x & y) << 1
            print("x:",bin(x))
            print("y:",bin(y))
        return bin(x)[2:]

a = Solution()
x, y =  "11011", "100011"
a.addBinary(x,y)