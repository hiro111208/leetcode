# Step 3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None

        val1 = root1.val if root1 else 0
        val2 = root2.val if root2 else 0
        merged_root = TreeNode(val1 + val2)

        merged_root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        merged_root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        return merged_root
```

1回目: 3分　7秒

2回目: 3分　8秒

3回目: 3分　9秒
