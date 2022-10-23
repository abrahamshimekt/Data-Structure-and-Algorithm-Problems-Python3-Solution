import heapq
def heap_sort(arr):
    heapq.heapify(arr)
    output = []
    while arr:
        output.append(heapq.heappop(arr))
    return output
print(f"{heap_sort([1,9,3,7])}")