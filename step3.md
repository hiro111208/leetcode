# Step 3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        min_depth = float("inf")
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if node:
                if node.left is None and node.right is None:
                    min_depth = min(min_depth, depth)
                else:
                    stack.append((node.left, depth + 1))
                    stack.append((node.right, depth + 1))
        return min_depth
```
1回目: 2分　11秒

2回目: 2分　6秒

3回目: 2分　8秒
