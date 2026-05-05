# Step 1

- Kadaneのアルゴリズムを使う

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = -float('inf')
        current_sum = 0
        for num in nums:
            current_sum = max(current_sum, 0)
            current_sum += num
            largest_sum = max(largest_sum, current_sum)
        return largest_sum

```

時間計算量: $O(n)$

空間計算量: $O(1)$
