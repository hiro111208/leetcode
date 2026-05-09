# Step 2

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

時間計算量: $O(n^2)$

空間計算量: $O(n)$
