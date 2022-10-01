print("Array Implementaion")

array = [10, 3, 7, 5]
array_2 = ['john', 10.0, 7, 3]
#this is called random accessing: indices starts with 0
print(array[1])
print(array[:])
print(array[0:2])
print(array[1:3])
print(array[:-1])
print(array[:-2])
print(array_2[0])
array_2[0] = 'adam'
print(array_2)

max = array[0]
#this is linear search : O(N)
for num in array:
    if num > max:
        max = num

print(f"max value in array is {max}")

min = array[0]
for num in array:
    if num < min:
        min = num

print(f"min value in array is {min}")

