# Step 3

- dequeを書き慣れていないのでBFSでStep 3を行う

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([[root, 1]])
        res = 0
        while queue:
            node, depth = queue.popleft()
            if node:
                res = depth
                queue.append([node.left, depth + 1])
                queue.append([node.right, depth + 1])
        return res
```

1回目: 1分　30秒

2回目: 1分　33秒

3回目: 1分　32秒
