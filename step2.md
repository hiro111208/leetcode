```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_counter = {}
        for num in nums:
            element_counter[num] = 1 + element_counter.get(num, 0)

        heap = []
        # keyをnum, valueをfrequencyと名付けた方がどちらが頻度かわかりやすい。
        for num, frequency in element_counter.items():
            heapq.heappush(heap, (frequency, num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for _, num in heap:
            res.append(num)

        return res
```
