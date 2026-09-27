# Step 2

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

時間計算量: O(n)

空間計算量: O(1)
