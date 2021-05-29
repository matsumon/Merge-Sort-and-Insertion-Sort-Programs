import time

# function: insertSortFunction
# purpose: sort an array of ints
# description: takes an array of ints and then sorts them by comparing elements to each other 
# and then inserting the higher element into its proper spot
def insertSortFunction(intArray):
	end = len(intArray)
	i = 1
	startTime = time.time();
	# While loop breaks when i is equal to the length of the array. This works because i is decremented at the very end
	while i < end:
		j = i - 1
		compare = i
		while j > -1 and j < end:
    		# if the jth element is greater than the ith element than insert the element
			#if (intArray[i] >= intArray[i]):
			if intArray[compare] >= intArray[j]:
				temp = intArray[compare] 
				intArray.pop(compare)
				compare = j
				intArray.insert(j,temp)
				#  If j is less than or equal to i then increment j only
				j = j - 1

			else:
				break;
		i = i+1
	endTime = time.time();
	print("n = ",end," Time = ",endTime-startTime)
	return intArray
# open input file
file = open("data.txt","r")
# open output file
outputFile= open("insert.out","a")
for line in file:
    # replace new lines and then make a string into an array
	line = line.replace("\n", "")
	intArray = line.split(" ")
	intArray = [int(i) for i in intArray]
	intArray.pop(0)
	array = insertSortFunction(intArray)
	# Turn array back into a string and remove uneeded chars
	string = str(array)
	string = string.strip("[]")
	string = string.replace("'","")
	string = string.replace(",","")
	string = string + "\n"
	outputFile.write(string)


