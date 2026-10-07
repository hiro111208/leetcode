# Step 3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def dfs(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, float('-inf'), float('inf'))
```

1回目: 1分　39秒

2回目: 1分　45秒

3回目: 1分　26秒
