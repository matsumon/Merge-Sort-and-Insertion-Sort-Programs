from random import seed
from random import randint
import time

# description: takes an array of ints and then sorts them by comparing elements to each other 
# and then inserting the higher element into its proper spot
def insertSortFunction(intArray):
	end = len(intArray)
	i = 1
	# While loop breaks when i is equal to the length of the array. This works because i is incremented at the very end
	while i < end:
		j = i - 1
		compare = i
		while j > -1 and j < end:
    		# if the ith element is greater than the ith element than insert the element
			if intArray[compare] >= intArray[j]:
				temp = intArray[compare] 
				intArray.pop(compare)
				compare = j
				intArray.insert(j,temp)
				j = j - 1

			else:
				break;
		i = i+1
	return intArray
# Generates an array of a given input
def generateRandom(n):
	seed(1)
	i = 0;
	intArray = []
	while i<n:
		intArray.append(randint(0,10000))		
		i = i+1
	return intArray
intArray = generateRandom(5000)
start = time.time()
intArray = insertSortFunction(intArray)
end = time.time()
print("n: 5000" " time: ", end-start)
intArray = generateRandom(10000)
start = time.time()
intArray = insertSortFunction(intArray)
end = time.time()
print("n: 10000" " time: ", end-start)
intArray = generateRandom(15000)
start = time.time()
intArray = insertSortFunction(intArray)
end = time.time()
print("n: 15000" " time: ", end-start)
intArray = generateRandom(20000)
start = time.time()
intArray = insertSortFunction(intArray)
end = time.time()
print("n: 20000" " time: ", end-start)

