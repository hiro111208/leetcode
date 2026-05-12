# Step 1

- 0を探すポインタと0以外を探すポインタを使う
- 0に遭遇したら、そのインデックスの1つ先から0以外を探す
- 0以外を見つけたら、その値と前述で見つけた0を入れ替える

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 1
        while l < len(nums) and r < len(nums):
            if nums[l] != 0:
                l += 1
                continue
            r = l + 1
            while r < len(nums):
                if nums[r] == 0:
                    r += 1
                else:
                    nums[l], nums[r] = nums[r], nums[l]
                    break
```

時間計算量: O(n^2)

空間計算量: O(1)
