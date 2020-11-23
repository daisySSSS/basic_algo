from sort import Sort

s = Sort()

nums = [134,13,15,15,64,14,73,42,14,82]
s.quick_sort(nums, 0, len(nums)-1)
print('='*15)
print('Result from quick sort')
print(nums)

nums = [134,13,15,15,64,14,73,42,14,82]
s = Sort()
s.heap_sort(nums)
print('='*15)
print('Result from heap sort')
print(nums)

nums = []
s = Sort()
s._build_heap(nums)
s.priority_queue_insert(nums, 100)
s.priority_queue_insert(nums, 134)
s.priority_queue_insert(nums, 33)
s.priority_queue_insert(nums, 1345)
s.priority_queue_insert(nums, 1)
s.priority_queue_insert(nums, 10)
print('='*15)
print('Result for priority queue insert')
print(nums)

max_heap = s.priority_queue_heap_extract_maximum(nums)
print('='*15)
print('Result for priority queue extract maximum')
print(max_heap)
print(nums)

nums = [134,13,15,15,64,14,73,42,14,82]
count_sort, idx = s.count_sort([(x, i) for i, x in enumerate(nums)])
print('='*15)
print('Result for count sort')
print(count_sort)

nums = [134,13,15,15,64,14,73,42,14,82]
radix_sort = s.radix_sort(nums)
print('='*15)
print('Result for radix sort')
print(radix_sort)
