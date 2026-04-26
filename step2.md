# Step 2

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l, r):
            if l > r:
                return None
            middle_index = (l + r) // 2
            root = TreeNode(nums[middle_index])
            root.left = helper(l, middle_index - 1)
            root.right = helper(middle_index + 1, r)
            return root
        return helper(0, len(nums) - 1)
```
