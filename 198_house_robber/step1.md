# Step 1

- $house(n)$まで訪れた時の最大の額$maxAmount(n)$は、$max(house(n) + maxAmount(n-2), maxAmount(n-1))$である

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 問題の制約でnumsのサイズが１以上は保証されているので、0は考慮しない
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

時間計算量: $O(n)$

空間計算量: $O(1)$
