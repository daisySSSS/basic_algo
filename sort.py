INF = 1E4

class Sort:
    def _exchange(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def _partition(self, nums, start, end):
        x = nums[end]
        i = start - 1
        j = start - 1
        for v in nums[start:end]:
            j += 1
            if v <= x:
                i += 1
                self._exchange(nums, i, j)
        i += 1
        self._exchange(nums, i, end)
        return i
                
    def quick_sort(self, nums, start, end):
        if start < end:
            q = self._partition(nums, start, end)
            self.quick_sort(nums, start, q-1)
            self.quick_sort(nums, q+1, end)
    
    def _max_heapify(self, nums, i):
        left = 2*i + 1
        right = 2*(i + 1)
        largest = i
        if left <  self._heap_size and nums[left] > nums[i]:
            largest = left
        if right < self._heap_size and nums[right] >  nums[largest]:
            largest = right
        if largest != i:
            self._exchange(nums, i, largest)
            self._max_heapify(nums, largest)

    def _build_heap(self, nums):
        self._heap_size = len(nums)
        for i in reversed(range(int(len(nums)/2.))):
            self._max_heapify(nums, i)

    def heap_sort(self, nums):
        self._build_heap(nums)
        for i in reversed(range(1, len(nums))):
            self._exchange(nums, i, 0)
            self._heap_size -= 1
            self._max_heapify(nums, 0)
    
    def priority_queue_increase_key(self, nums, i, key):
        if key <= nums[i]:
            return False
        else:
            nums[i] = key
            parent = int((i-1)/2.)
            while i and nums[parent] < nums[i]:
                self._exchange(nums, parent, i)
                i = parent
                parent = int((i-1)/2.)

    def priority_queue_heap_extract_maximum(self, nums):
        if self._heap_size < 1:
            return False
        max_heap = nums[0]
        nums[0] = nums[self._heap_size-1]
        self._heap_size -= 1
        self._max_heapify(nums, 0)
        return max_heap
    
    def priority_queue_heap_max(self, nums):
        if self._heap_size < 1:
            return False
        return nums.pop(0)

    def priority_queue_insert(self, nums, key):
        self._heap_size += 1
        nums.append(-INF)
        self.priority_queue_increase_key(nums, self._heap_size-1, key)

    def count_sort(self, nums):
        mi = min([x[0] for x in nums])
        ma = max([x[0] for x in nums])       
        cnt = dict()
        for i in range(mi, ma+1):
            cnt[i] = 0
        for i in nums:
            cnt[i[0]] += 1
        prv = -1
        for i in range(mi, ma+1):
            cnt[i] += prv
            prv = cnt[i]
        
        lnums = len(nums)
        result = [None]*lnums
        attached = [None]*lnums
        for v in reversed(nums):
            result[cnt[v[0]]] = v[0]
            attached[cnt[v[0]]] = v[1]
            cnt[v[0]] -= 1
        return result, attached 

    def _split(self, num):
        return [int(i) for i in str(num)]

    def radix_sort(self, nums):
        splited_num = [self._split(num) for num in nums]
        cnt_num = [len(x) for x in splited_num]
        max_cnt = max(cnt_num)
        splited_num = [[0]*(max_cnt-len(x))+x for x in splited_num]
        cnt = max_cnt-1
        idx = list(range(len(nums)))
        while cnt >=0:
            num_to_sort =  [(splited_num[i][cnt],i) for i in idx]
            _, idx = self.count_sort(num_to_sort)
            cnt -= 1
        return [nums[i] for i in idx]
        
    # def bucket_sort(self, nums):
    # def bubble_sort():
    # def insertion_sort():