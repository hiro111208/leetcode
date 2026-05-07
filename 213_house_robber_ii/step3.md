# Step 3

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        def rob_linear(start, end):
            profit_two_back = nums[start]
            profit_one_back = max(nums[start], nums[start + 1])

            for i in range(start + 2, end):
                current_profit = max(profit_one_back, profit_two_back + nums[i])
                profit_two_back = profit_one_back
                profit_one_back = current_profit

            return profit_one_back

        return max(rob_linear(0, len(nums) - 1), rob_linear(1, len(nums)))

```

1回目: 2分　57秒

2回目: 2分　18秒

3回目: 2分　14秒
