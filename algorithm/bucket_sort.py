# as defined, bucket_sort only work for float and can only run linear in range [0,1)
def bucket_sort(input_array, bucket_num):
	max_value = max(input_array)
	min_value = min(input_array)
	diff = (max_value - min_value) / bucket_num
	if diff == 0:
		print('too many buckets, please make it fewer than ' + str(diff))
		return
	buckets = []
	result = [[] for i in range(bucket_num)]
	bound = min_value + diff
	buckets.append(bound)
	while buckets[-1] < max_value:
		bound += diff
		buckets.append(bound)
	for index in range(len(buckets)):
		for i in range(len(input_array)):
			if input_array[i] and input_array[i] <= buckets[index]:
				result[index].append(input_array[i])
				input_array[i] = None
	for i in range(len(result)):
		result[i] = insertion_sort(result[i])
	complete_result = []
	for i in range(len(result)):
		complete_result += result[i]
	return complete_result

def insertion_sort(input_array):
	for i in range(1, len(input_array)):
		target = input_array[i]
		prev = i-1
		while target < input_array[prev] and prev >= 0:
			input_array[prev+1] = input_array[prev]
			prev -= 1
		input_array[prev+1] = target
	return input_array
print(bucket_sort([0.2, 0.1, 0.53, 0.44, 0.88, 0.99, 0.36], 3))
