# Step 2

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        if pivot != -1:
            for i in range(len(nums) - 1, pivot, -1):
                if nums[i] > nums[pivot]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    break

        left_pointer = pivot + 1
        right_pointer = len(nums) - 1
        while left_pointer < right_pointer:
            nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
            left_pointer += 1
            right_pointer -= 1
```

時間計算量: O(n)

空間計算量: O(1)
