# assume the sorted array start from the lowest value to the highest
def binary_search(val, input_array):
	size = len(input_array)
	if size == 1 and input_array[0] != val:
		print('there is no such value exist')
		return
	mid = size // 2
	if input_array[mid] > val:
		return binary_search(val, input_array[0:mid])
	elif input_array[mid] < val:
		result = binary_search(val, input_array[mid+1:size])
		if type(result) is not int:
			return result
		return mid+1+result
	return mid

list = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(10, list))
print(binary_search(22, list))
print(binary_search(-1, list))
