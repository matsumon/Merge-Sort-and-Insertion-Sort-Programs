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
# open input file
file = open("data.txt","r")
# open output file
outputFile= open("merge.out","a")
for line in file:
    # get rid of newline and then make a string into an array
	line = line.replace("\n", "")
	intArray = line.split(" ")
	# get rid of first element
	intArray.pop(0)
	# I got this from Stack Overflow, but it turns an array of strings into an array of ints
	# It does this by going through each element in the array and running the int function on it
	# Another possible solution would be to use map, but many sources told me it was deprecated
	intArray = [int(i) for i in intArray]
	end = len(intArray)
	start = time.time();
	array = recursiveFunction(intArray)
	endTime = time.time();
	print("n:", end, "time:",endTime - start)
	# make array back into a string and get rid of the brackets and commas
	string = str(array)
	string = string.strip("[]")
	string = string.replace(",","")
	string = string + "\n"
	# write results into output file.
	outputFile.write(string)

