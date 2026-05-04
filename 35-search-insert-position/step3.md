# Step 3

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            middle = start + (end - start) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                end = middle - 1
            else:
                start = middle + 1
        return start
```

1回目: 1分　31秒

2回目: 1分　26秒

3回目: 1分　27秒
