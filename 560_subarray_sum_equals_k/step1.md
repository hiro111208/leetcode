# Step 1

## Approach 1

- 二重ループで解く

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        num_subarrays = 0
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                if current_sum == k:
                    num_subarrays += 1
        return num_subarrays
```

時間計算量: $O(n^2)$

空間計算量: $O(1)$

- しかし上記ではTime Limit Exceededになった。

## Approach 2

- ある地点iまでの合計から、iより前の地点jまでの合計を引いてkの個数をカウントする
- 過去の合計とそれが出た回数を記録しておく
- kからある地点での合計を引いた値が記録にあったら記録の回数を戻り値に足していく

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_to_count = {0: 1}
        prefix_sum = 0
        num_subarrays = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_sum_to_count:
                num_subarrays += prefix_sum_to_count[prefix_sum - k]
            prefix_sum_to_count[prefix_sum] = prefix_sum_to_count.get(prefix_sum, 0) + 1

        return num_subarrays

```

時間計算量: $O(n)$

空間計算量: $O(n)$
