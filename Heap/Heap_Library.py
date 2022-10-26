import heapq

# heap = [4, 7, 3, -1, 0, -4]
#
# heapq.heapify(heap)
# print(heap)

nums = [4, 7, 3, -1, 0, -4]
heap = []
for value in nums:
    heapq.heappush(heap, value)

while heap:
    print(heapq.heappop(heap))
# print(heap)