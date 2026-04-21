# Step 1

1. nums1から重複を取り除く
2. nums2でループを回し、整数がnums1にあったらその数をresに追加、nums1から除外

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1_without_duplicates = {num for num in nums1}
        for num in nums2:
            if num in nums1_without_duplicates:
                res.append(num)
                nums1_without_duplicates.remove(num)
        return res

```

時間計算量: O(n)
空間計算量: O(n)
