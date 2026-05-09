# Step 3

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis_from_i = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(nums) - 1, i, -1):
                if nums[i] < nums[j]:
                    lis_from_i[i] = max(lis_from_i[i], 1 + lis_from_i[j])

        return max(lis_from_i)

```

1回目: 1分　17秒

2回目: 1分　23秒

3回目: 1分　14秒
