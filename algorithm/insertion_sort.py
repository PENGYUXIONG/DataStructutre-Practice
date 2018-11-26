def insert_sort(sample_array):
	for index in range(1, len(sample_array)):
		target_val = sample_array[index]
		prev_index = index - 1
		while prev_index >= 0 and sample_array[prev_index] > target_val:
			sample_array[prev_index+1] = sample_array[prev_index]
			prev_index = prev_index - 1
		sample_array[prev_index+1] = target_val
	return sample_array

sample_list = [1,-1,0,6,3]
print(insert_sort(sample_list))


