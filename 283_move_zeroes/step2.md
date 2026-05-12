# Step 2

- Step 1のコードは遅い
- rのインデックスを毎回lの1個先にリセットしないようにしたい

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0
        while l < len(nums) and r < len(nums):
            if nums[l] != 0:
                l += 1
                r = max(r, l)
                continue
            while r < len(nums):
                if nums[r] == 0:
                    r += 1
                else:
                    nums[l], nums[r] = nums[r], nums[l]
                    break

```

時間計算量: $O(n)$

空間計算量: $O(1)$

- 他の人のコード見たらもっとスマートなのがあった
- 0でない値が次にどのインデックスに来るか変数で持つ
- 変数は0で始まり、0でない値がみつかったら、変数が示すインデックスに格納されている値と入れ替える

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
                zero_index += 1

```
時間計算量: $O(n)$

空間計算量: $O(1)$