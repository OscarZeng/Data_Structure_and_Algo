def main():
    n = int(input())
    #print(n)
    
    nums = input().split()
    for j in range(len(nums)):
    	nums[j] = int(nums[j])
    #print(nums)
    
    the_maximal = max(nums)
    #print(the_maximal)
    primesNums = []
    #Generate prime numbers for the_maximal
    primes = [True] * the_maximal
    for a in range(2, the_maximal):
        if primes[a-1]:
            for j in range(a+a, the_maximal, a):
                primes[j-1] = False
    #print(primes)
    for i in range(2,the_maximal+1):
        if primes[i-1]:
            primesNums.append(i)
    #now we have the primenumbers
    #print(primesNums)

    #Append the actual number as the last element at the end of list
    
    tupleAns = []
    
    for ind in range(len(nums)):
    	currentNum = nums[ind]
    	primeFacts = []
    	while currentNum != 1:
    		for p in primesNums:
    			if currentNum%p == 0:
    				primeFacts.append(p)
    				currentNum = currentNum/p
    				#print(currentNum, p)
    				break
    	#print(primeFacts)
    	tupleAns.append((primeFacts, nums[ind]))
    #tupleAns will record all of the primefacts and the number it self in a tuple.
    #So we can sort the tuple and print out the second element of the tuple.
    tupleAns.sort()
    for t in tupleAns:
    	print(t)




if __name__ == '__main__':
    main()