# Step 3

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        max_amount_prev_2 = nums[0]
        max_amount_prev_1 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            max_amount = max(max_amount_prev_1, nums[i] + max_amount_prev_2)
            max_amount_prev_2 = max_amount_prev_1
            max_amount_prev_1 = max_amount
        return max_amount_prev_1
```

1回目: 1分　46秒

2回目: 1分　58秒

3回目: 1分　47秒
