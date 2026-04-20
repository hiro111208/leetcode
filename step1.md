# Step 1

- forループで各整数を見ていく
- targetから自身を引いた数が過去に現れたか確認する
- あればその数のインデックスと自身のインデックスを返し、なければ自身をキー、インデックスを値としてハッシュテーブルに保存していく

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

- 時間計算量: O(n)
- 空間計算量: O(n)
