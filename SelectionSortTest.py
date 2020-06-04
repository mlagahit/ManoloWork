# Array for sorting selection

array = [13, 4, 9, 5, 3, 16, 12]

# creating function for selectionsort

def selectionSort(array):

	n = len(array) # checks length of array

	for i in range(n): # for loop runs for every element in the range of the array

		# Initially assume the first element of the unsorted part is the minimum

		minimum = i # minimum number in array is set as i 

		for j in range(i+1, n):

			if (array[j] < array[minimum]): # comparison operator of the 2 values 

			minimum = j # minimum is now j

		# swaps the minimum in i to the minimum in j

		temp = array[i]
		array[i] = array[minimum]
		array[minimum] = temp

	return array

print(selectionSort(array))
