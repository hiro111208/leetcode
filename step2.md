# Step 2

## Iterative DFS

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

        nodes_and_sums = [(root, root.val)]
        while nodes_and_sums:
            node, current_sum = nodes_and_sums.pop()
            if node:
                if node.left is None and node.right is None and current_sum == targetSum:
                    return True
                if node.left is not None:
                    nodes_and_sums.append((node.left, current_sum + node.left.val))
                if node.right is not None:
                    nodes_and_sums.append((node.right, current_sum + node.right.val))
        return False
```

時間計算量: O(n)

空間計算量: O(n)

## Recursive DFS

- 他の人のコードを拝見

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, current_sum):
            if node is None:
                return False

            current_sum += node.val
            if node.left is None and node.right is None:
                return current_sum == targetSum
            return dfs(node.left, current_sum) or dfs(node.right, current_sum)
        return dfs(root, 0)
```

時間計算量: O(n)

空間計算量: O(n)
