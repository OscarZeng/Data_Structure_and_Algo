### This function is to convert the binary code into sentences using ASCII code###

def convertBinaryToSentence(binaryStrIn):
	ans = ""
	binarys = binaryStrIn.split()
	for i in binarys:
		ans = ans + chr(int(i,2))

	print(ans)
	return ans

binaryStrIn = "01010011 01101111 01100110 01110100 01110111 01100001 01110010 01100101 00100000 01000100 01100101 01110110 01100101 01101100 01101111 01110000 01100101 01110010"
convertBinaryToSentence(binaryStrIn)