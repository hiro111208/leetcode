# Step 1

## Approach 1

### Explanation

### Code

```python
class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[l] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return res
```

時間計算量:

空間計算量:
