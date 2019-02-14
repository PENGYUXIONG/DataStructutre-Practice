def counting_sort(input_array):
	min_val = min(input_array)
	max_val = max(input_array)
	size = max_val - min_val + 1
	
	count = [0 for i in range(size)]
	output = [0 for i in range(size)]
	
	for i in input_array:
		count[i-min_val] = count[i-min_val] + 1
	for i in range(1, size):
		count[i] = count[i] + count[i-1]
	for i in input_array:
		if count[i-min_val] != 0:
			output[count[i-min_val] - 1] = i
			count[i-min_val] = count[i-min_val] - 1
	return output
	print(output)

counting_sort([4, 2, 3])
