def selection_sort(sample_array, cur_pos = 0):
	if not sample_array:
		print('empty array!')
		return

	if cur_pos >= len(sample_array)-1:
		return sample_array

	for i in range(cur_pos+1, len(sample_array)):
		if sample_array[i] < sample_array[cur_pos]:
			sample_array[cur_pos], sample_array[i] = sample_array[i], sample_array[cur_pos]
	cur_pos = cur_pos + 1
	return selection_sort(sample_array, cur_pos)


sample_array = [2,-1,3, 9, 0, -5]
selection_sort(sample_array)
print(sample_array)


def selection_sort_new(sample_array):
	for cur_pos in range(len(sample_array)):
		for i in range(cur_pos+1, len(sample_array)):
			if sample_array[cur_pos] > sample_array[i]:
				sample_array[i], sample_array[cur_pos] = sample_array[cur_pos], sample_array[i]
	return sample_array


sample_array = [1, 2, -1, 3]
print(selection_sort_new(sample_array))
