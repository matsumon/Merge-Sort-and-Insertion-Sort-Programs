from random import seed
from random import randint
import time
# function: recursiveFunction
# purpose: sort a given array of numbers
# description: Sorts by splitting an array in half until it hits the base case of 1 element
# 	Afterwards the elements are sorted by adding the highest of the left and right array.
def recursiveFunction(array):
	middle = len(array)//2
	if (middle == 0):
		return(array)
	else:
		left = array[int(middle):] 
		right = array[:int(middle)]

		left = recursiveFunction(left)
		right = recursiveFunction(right)
		i = 0
		j = 0
		combined= []
		while((len(array)) != (i+j)):
    		# no more elements in the left array so the right array is concatenated onto the return array
			if(i==len(left)):
				combined= combined + right[j:]
				break
    		# no more elements in the right array so the left array is concatenated onto the return array
			elif(j==len(right)):
				combined= combined + left[i:]
				break
			# checks elements and if the left is larger than the right the left element is returned
			if (left[i] > right[j]):
				combined.append(left[i])
				i= i +1
			# checks elements and if the right is larger than the left the right element is returned
			elif(right[j] >= left[i]):
				combined.append(right[j])
				j= j +1
		return combined
# Generates an array of a given input
def generateRandom(n):
	seed(1)
	i = 0;
	intArray = []
	while i<n:
		intArray.append(randint(0,10000))		
		i = i+1
	return intArray
#generate random number array
intArray = generateRandom(5000)
#start time
start = time.time()
#sort
intArray = recursiveFunction(intArray)
#stop timer
end = time.time()
print("n: 5000" " time: ", end-start)
intArray = generateRandom(10000)
start = time.time()
intArray = recursiveFunction(intArray)
end = time.time()
print("n: 10000" " time: ", end-start)
intArray = generateRandom(15000)
start = time.time()
intArray = recursiveFunction(intArray)
end = time.time()
print("n: 15000" " time: ", end-start)
intArray = generateRandom(20000)
start = time.time()
intArray = recursiveFunction(intArray)
end = time.time()
print("n: 20000" " time: ", end-start)

