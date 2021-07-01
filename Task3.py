
def first(arr, low, high, x, n) :
	if (high >= low) :
		mid = low + (high - low) // 2; # (low + high)/2;
		if ((mid == 0 or x > arr[mid-1]) and arr[mid] == x) :
			return mid
		if (x > arr[mid]) :
			return first(arr, (mid + 1), high, x, n)
		return first(arr, low, (mid -1), x, n)
		
	return -1
	
# function for sorting array A1 on the basis of A2
def sortAccording(A1, A2, m, n) :


	temp = [0] * m  #temp array 
	visited = [0] * m
	
	for i in range(0, m) :
		temp[i] = A1[i]
		visited[i] = 0

	
	temp.sort() 
	
	# for index of output which is sorted A1[]
	ind = 0

# mapping array A2 elements in the array A1
	for i in range(0, n) :
		
		# Find index of the first occurrence
		# of A2[i] in temp
		f = first(temp, 0, m-1, A2[i], m)

		# If not present, no need to proceed
		if (f == -1) :
			continue

		# Copy all occurrences of A2[i] to A1[]
		j = f
		while (j<m and temp[j]== A2[i]) :
			A1[ind] = temp[j];
			ind = ind + 1
			visited[j] = 1
			j = j + 1
	
	# Now copy all items of temp[] which are
	# not present in A2[]
	for i in range(0, m) :
		if (visited[i] == 0) :
			A1[ind] = temp[i]
			ind = ind + 1
			
# output 
def printArray(arr, n) :
	for i in range(0, n) :
		print(arr[i], end = " ")
	print("")
	

A1=["ele11","ele2","ele9","ele7","ele12","ele9","ele4","ele5","ele10","ele13","ele8"]

A2=["ele1","ele3","ele2","ele11","ele7","ele10"]
m = len(A1)
n = len(A2)
print("Sorted array is ")
sortAccording(A1, A2, m, n)
printArray(A1, m)