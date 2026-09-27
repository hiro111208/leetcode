# Step 1

## Approach 1

### Explanation

### Code

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        res = float("inf")
        l, total = 0, 0
        for r, num in enumerate(nums):
            total += num
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1
        return 0 if res == float("inf") else res
```

時間計算量:

空間計算量:
