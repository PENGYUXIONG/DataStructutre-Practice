def quick_sort(input_array, low, high):
        # record the low end position
        old_low = low
        for i in range(low+1, high):
            # if there is smaller number on the right side
            if input_array[low] > input_array[i]:
                # swap the right neighbor to the smaller number, then swap pivot to its right
                input_array[low+1], input_array[i] = input_array[i], input_array[low+1]
                input_array[low+1], input_array[low] = input_array[low], input_array[low+1]
                low += 1
        # if there is no number to sort then break
        if low >= high:
            return
        quick_sort(input_array, old_low, low)
        quick_sort(input_array, low+1, high)
        return input_array


Input = [2,6,3,8,2,98,1,9,0]
print(quick_sort(Input, 0, len(Input)))
