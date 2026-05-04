# Step 1

- 二分探索で解く

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start_index, end_index = 0, len(nums) - 1
        while start_index <= end_index:
            middle_index = (start_index + end_index) // 2
            if nums[middle_index] == target:
                return middle_index
            elif nums[middle_index] < target:
                start_index = middle_index + 1
            else:
                end_index = middle_index - 1
        return start_index
```

時間計算量: $O(\log n)$

空間計算量: $O(1)$
