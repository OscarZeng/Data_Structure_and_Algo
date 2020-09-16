#Please implement check sum function which will return True if the sum of two given parameter is greater than or equal 20
def checkSum(a,b):
	if (a + b)%2 == 0:
		return True
	else:
		return False


a = 10
b = 14
ans = checkSum(a, b)
print("a= "+ str(a)+"\nb= "+str(b) + "\nans= " + str(ans))
for a in range(1,10):
	for b in range(3,7):
		print("a=",a,"  b=", b)
		print("(a+b)/3=", float((a+b)/3))
		print("(a+b)%3=", (a + b)%3)

