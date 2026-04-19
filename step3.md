# Step 3

```python
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = [[nums1[i] + nums2[0], i, 0] for i in range(len(nums1))]
        heapq.heapify(min_heap)
        res = []

        while min_heap and k > 0:
            _, index1, index2 = heapq.heappop(min_heap)
            res.append([nums1[index1], nums2[index2]])
            k -= 1

            if index2 + 1 < len(nums2):
                heapq.heappush(min_heap, [nums1[index1] + nums2[index2 + 1], index1, index2 + 1])

        return res
```
