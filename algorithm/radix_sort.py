def radix_sort(input_array):
	max_value = max(input_array)
	min_value = None
	index = []
	negative_inputs = []
	for i in input_array:
		if i < 0:
			negative_inputs.append(0-i)

	for i in negative_inputs:
		input_array.remove(0-i)	

	if negative_inputs != []:
		min_value = max(negative_inputs)


	exp = 1
	while max_value > 0:
		max_value = max_value / 10
		input_array = counting_sort(input_array, exp)
		exp = exp * 10

	if min_value:
		neg_exp = 1
		while min_value > 0:
			min_value = min_value / 10
			negative_inputs = counting_sort(negative_inputs, neg_exp)
			neg_exp *= 10
		negative_inputs.reverse()
		for i in range(len(negative_inputs)):
			negative_inputs[i] = 0 - negative_inputs[i]

	return negative_inputs + input_array

def counting_sort(input_array, exp):
	size = len(input_array)

	output = [0 for i in range(size)]
	count = [0] * 10
	
	for i in input_array:
		count[i/exp%10] += 1
		
	for i in range(1, 10):
		count[i] = count[i] + count[i-1]
	counter = size
	while counter > 0:
		counter -= 1
		output[count[input_array[counter]/exp%10]-1] = input_array[counter]
		count[input_array[counter]/exp%10] -= 1
	return output

print(radix_sort([321, 2, 4, 1, 23, 31, 122, 0, -12, -21]))
