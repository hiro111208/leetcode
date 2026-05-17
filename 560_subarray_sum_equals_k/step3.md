# Step 3

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_to_count = {0: 1}
        prefix_sum = 0
        num_subarrays = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_sum_to_count:
                num_subarrays += prefix_sum_to_count[prefix_sum - k]
            prefix_sum_to_count[prefix_sum] = prefix_sum_to_count.get(prefix_sum, 0) + 1

        return num_subarrays

```

1回目: 2分　5秒

2回目: 1分　44秒

3回目: 1分　31秒
