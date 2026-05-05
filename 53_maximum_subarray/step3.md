# Step 3

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = -float('inf')
        current_sum = 0
        for num in nums:
            current_sum = max(current_sum, 0) + num
            largest_sum = max(largest_sum, current_sum)
        return largest_sum

```

1回目: 1分　26秒

2回目: 1分　8秒

3回目: 1分　5秒
