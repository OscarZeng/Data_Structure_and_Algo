p = "a********************b"

while p.find("**") != -1:
	p = p.replace("**", "*")
	print(p)