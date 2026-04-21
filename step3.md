# Step 3

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1_without_duplicates = set(nums1)
        for num in nums2:
            if num in nums1_without_duplicates:
                res.append(num)
                nums1_without_duplicates.remove(num)
        return res
```
