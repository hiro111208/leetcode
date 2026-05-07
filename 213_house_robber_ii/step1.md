# Step 1

- $i$番目まで訪れた時の最大利益$maxAmount[i]$は$max(maxAmount[i - 1], maxAmount[i - 2] + nums[i])$
- 円形のため、$0\le i \le nums.size -2$の範囲の最大利益と$1\le i \le nums.size -1$の範囲の最大利益のうち大きい方を返す

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        first_max_amount_prev_2 = nums[0]
        first_max_amount_prev_1 = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            current_max_amount = max(first_max_amount_prev_1, first_max_amount_prev_2 + nums[i])
            first_max_amount_prev_2 = first_max_amount_prev_1
            first_max_amount_prev_1 = current_max_amount

        second_max_amount_prev_2 = nums[1]
        second_max_amount_prev_1 = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            current_max_amount = max(second_max_amount_prev_1, second_max_amount_prev_2 + nums[i])
            second_max_amount_prev_2 = second_max_amount_prev_1
            second_max_amount_prev_1 = current_max_amount
        return max(first_max_amount_prev_1, second_max_amount_prev_1)
```

時間計算量: $O(n)$

空間計算量: $O(1)$
