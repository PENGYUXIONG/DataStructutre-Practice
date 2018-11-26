def bubble_sort(sample_array):
	swap_boolean = False

	for i in range(len(sample_array)):
		for prev_pos in range(len(sample_array)-i-1):
			cur_pos = prev_pos + 1
			if sample_array[prev_pos] > sample_array[cur_pos]:
				sample_array[prev_pos], sample_array[cur_pos] = sample_array[cur_pos], sample_array[prev_pos]
				swap_boolean = True
		if not swap_boolean:
			break
	
	return sample_array


sample_array = [4, 1, 2, -5, -7, -3, 0]
print(bubble_sort(sample_array))
