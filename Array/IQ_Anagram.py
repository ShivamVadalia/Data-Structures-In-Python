import timeit

def is_anagram(subject, anagram):
    subject_list = list(subject)
    anagram_list = list(anagram)
    for x in subject_list:
        if x in anagram_list:
            anagram_list.remove(x)
    if len(anagram_list) == 0:
        print("It is an anagram")
    else:
        print("It is not an anagram")

#Below code is used to get execution time
result = timeit.timeit(stmt='is_anagram("secure", "rescue")', globals=globals(), number=4)
print(f"Execution time is {result / 4} seconds")
# is_anagram("secure", "rescue")
# is_anagram("tower", "wreto")

