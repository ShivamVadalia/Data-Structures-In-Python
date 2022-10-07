array = [1, 2, 3, 4, 5]
array_2 = [1, 2, 3, 4, 5, 6]


def reverse_array(arr):
    # pointing to first item
    startindex = 0
    # pointing to last item
    endindex = len(arr) - 1
    while startindex < endindex:
        # keep swapping the items
        arr[startindex], arr[endindex] = arr[endindex], arr[startindex]
        startindex += 1
        endindex -= 1
    print(arr)


reverse_array(array)
reverse_array(array_2)
