def main():
	n = int(input())
	#print(n)

	instructions = []
	for i in range(n):
		line = (input())
		instructions.append(line.split())
	#print(instructions)

	#define the four directions(where heads towards), right, up, left, down
	directions = [(1,0), (0,1), (-1,0), (0,-1)]
	for ins in instructions:
		numMoves = ins[0]
		moves = ins[1]
		#print(numMoves, moves)
		#Here we use a list to store the locations of the snack
		#With the initial value of 1,1
		#The head will be front snackLen[-1] while the tail is snackLen[0]
		snackLen = [(0,0)]
		#Set the initial direction
		direction = 0
		steps = 0
		for m in moves:
			biten = False
			steps += 1
			#Change the direction first, since snack will always move forward
			#left is +1 
			if m == "L":
				if direction == 3:
					direction = 0
				else:
					direction += 1
			elif m == "R":
				if direction == 0:
					direction == 3
				else:
					direction -= 1
			#Now the snack moves forward one step
			nextStep = (snackLen[-1][0]+directions[direction][0],snackLen[-1][1]+directions[direction][1])
			#print(nextStep)
			snackLen.append(nextStep)
			if m!="E":
				snackLen.pop(0)
			#print(snackLen,directions[direction])
			#Now check whether the snack eat itself
			if nextStep in snackLen[:-1]:
				print(steps)
				biten = True
				break

		if not biten:
			print("YES") 


			


if __name__ == '__main__':
	main()