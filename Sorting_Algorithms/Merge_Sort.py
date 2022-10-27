def merge_sort(nums):
    # define the base case: that we keep splitting the lists until
    # the sublists have just 1 item - arrays with a single item is sorted by default

    if len(nums) == 1:
        return

    # Divide Phase
    middle_index = len(nums) // 2
    left_half = nums[:middle_index]
    right_half = nums[middle_index:]

    merge_sort(left_half)
    merge_sort(right_half)

    # Conquer Phase
    i = 0
    j = 0
    k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            nums[k] = left_half[i]
            i += 1
        else:
            nums[k] = right_half[j]
            j += 1
        k += 1

    # After that there may be additional items in the left or right sub-array
    while i < len(left_half):
        nums[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        nums[k] = right_half[j]
        j += 1
        k += 1


my_list = [45, 55, -10, 0, -45, 79]
merge_sort(my_list)
print(my_list)
