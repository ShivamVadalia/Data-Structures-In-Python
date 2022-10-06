import timeit

def palindrome_python(str):
    # pointing to first item
    startindex = 0
    # pointing to last item
    endindex = len(str) - 1
    while startindex < endindex:
        if str[startindex] == str[endindex]:
            flag = 1
        else:
            flag = 0
            break
        startindex += 1
        endindex -= 1
    if flag == 1:
        print("String is a palindrome")
    else:
        print("String is not a palindrome")
# result = timeit.timeit(stmt='palindrome_python("madam")', globals=globals(), number=4)
# print(f"Execution time is {result / 4} seconds")
palindrome_python("madam")