# Step 1

## Approach 1

### Explanation

Next permutation = the smallest sequence that is lexicographically larger than the current one (or the smallest overall if already the last).

1. Scan from the right and find the **pivot**: the rightmost index `i` with `nums[i] < nums[i + 1]`. The suffix after the pivot is non-increasing, so it is already the largest arrangement of those values.
2. If a pivot exists, scan the suffix from the right and swap the pivot with the **rightmost** value strictly greater than it (the smallest upgrade on a descending suffix).
3. Reverse the suffix after the pivot so it becomes ascending — the smallest possible continuation. If there is no pivot, the whole array is descending; reversing it yields the first permutation.

### Code

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
            for i in range(len(nums) - 1, pivot - 1, -1):
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
