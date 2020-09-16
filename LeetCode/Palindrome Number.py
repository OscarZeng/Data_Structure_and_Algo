#Using int convert to string, Own solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return (str(x) == str(x)[::-1]) if x>=0 else False

# Without using int convert to string
class Solution:
    def isPalindrome(self, x: int) -> bool:
    	#Special cases will fail like 12100, and we can know that any number multiple of 10 is False
        if x < 0 or (x%10 ==0 and x!= 0):
            return False
        secondhalf = 0
        while x > secondhalf:
            secondhalf = secondhalf*10 + x%10
            x = x//10
        return (secondhalf == x or secondhalf//10 == x)