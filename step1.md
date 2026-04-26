# Step 1

1. numsが空ならNoneを返す
2. rootはnumsの真ん中のindexの値
3. rootのleftは2のindexまでのnumsで再度2を繰り返す
4. rootのrightは2のindexより先のnumsで再度2を繰り返す

- 配列のスライスの仕方を正確に覚えていない

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        middle_index = (len(nums) - 1) // 2
        root = TreeNode(nums[middle_index])
        root.left = self.sortedArrayToBST(nums[:middle_index])
        root.right = self.sortedArrayToBST(nums[middle_index + 1:])
        return root
```

時間計算量: O(nlogn)

空間計算量: O(n)

- スライス使っているのが非効率そう
