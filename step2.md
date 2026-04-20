# Step 2

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = dict()
        for i, num in enumerate(nums):
            difference = target - num
            if difference in num_to_index.keys():
                return [i, num_to_index[difference]]
            else:
                num_to_index[num] = i
```
