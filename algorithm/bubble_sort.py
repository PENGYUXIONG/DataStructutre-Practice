def bubble_sort(sample_array):
	swap_boolean = False

	for prev_pos in range(len(sample_array)-1):
		cur_pos = prev_pos + 1
		if sample_array[prev_pos] > sample_array[cur_pos]:
			sample_array[prev_pos], sample_array[cur_pos] = sample_array[cur_pos], sample_array[prev_pos]
			swap_boolean = True
	if not swap_boolean:
		return sample_array
	
	return bubble_sort(sample_array)	


sample_array = [4, 1, 2, -5, -7, -3, 0]
print(bubble_sort(sample_array))
