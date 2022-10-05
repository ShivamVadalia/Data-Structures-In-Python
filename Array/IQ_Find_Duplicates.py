def find_duplicates(nums):
    #this method cannot handle negative numbers!!!
    #the maximum item is smaller than the size of the list
    for num in nums:
        if nums[abs(num)] >= 0:
            nums[abs(num)] = -nums[abs(num)]
        else:
            print(f"Repetition found: {str(abs(num))}")

find_duplicates([2, 6, 5, 4, 4, 3, 2, 1, 1])