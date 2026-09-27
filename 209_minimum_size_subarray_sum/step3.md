# Step 3

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        min_len = n + 1
        left, window_sum = 0, 0
        for right, num in enumerate(nums):
            window_sum += num
            while window_sum >= target:
                min_len = min(min_len, right - left + 1)
                window_sum -= nums[left]
                left += 1
        return 0 if min_len == n + 1 else min_len
```

1回目: 1分　25秒

2回目: 1分　30秒

3回目: 1分　29秒
