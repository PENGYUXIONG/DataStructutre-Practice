def merge_sort(sample_list):
	length = len(sample_list)
	if length == 0:
		print('empty Array!')
		return
	
	if length == 1:
		return sample_list	

	mid = get_mid(length)
	low_list = sample_list[:mid]
	high_list = sample_list[mid:]
	new_low_list = merge_sort(low_list)
	new_high_list = merge_sort(high_list)
	sample_list = merge(new_low_list, new_high_list)
	return sample_list


def get_mid(length):
	if length%2 != 0:
		length = length - 1
	mid = int(length / 2)
	return mid


def merge(low_array, high_array):
	return_list = []
	cur_low = 0
	cur_high = 0
	while cur_low < len(low_array) and cur_high < len(high_array):
		if low_array[cur_low] > high_array[cur_high]:
			return_list.append(high_array[cur_high])
			cur_high = cur_high + 1
		else:
			return_list.append(low_array[cur_low])
			cur_low = cur_low + 1
	if cur_low < len(low_array):
		return_list = return_list + low_array[cur_low:]

	elif cur_high < len(high_array):
		return_list = return_list + high_array[cur_high:]
	return return_list


sample_array = [3, 1, -1, -2, -4, -6, 5, 0]
print(merge_sort(sample_array))
