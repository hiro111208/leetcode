# Step 1

- recursionで試したが、上手くいかなかったのでまずiterativeで試す

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        stack = [(root, root.val)]
        while stack:
            node, current_sum = stack.pop()
            if node:
                if node.left is None and node.right is None and current_sum == targetSum:
                    return True
                if node.left is not None:
                    stack.append((node.left, current_sum + node.left.val))
                if node.right is not None:
                    stack.append((node.right, current_sum + node.right.val))
        return False
```

時間計算量: O(n)

空間計算量: O(n)
