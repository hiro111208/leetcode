# Step 2

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_to_count = {0: 1}
        prefix_sum = 0
        num_subarrays = 0

        for num in nums:
            prefix_sum += num
            num_subarrays += prefix_sum_to_count.get(prefix_sum - k, 0)
            prefix_sum_to_count[prefix_sum] = prefix_sum_to_count.get(prefix_sum, 0) + 1

        return num_subarrays

```

時間計算量: $O(n)$

空間計算量: $O(n)$
