# Step 1

- 漸化式を作れなかった
- [NeetCode](https://www.youtube.com/watch?v=cjWnW0hdF1Y)の解法を見た
  - LIS[i] を「nums[i] から始まる最長増加部分列の長さ」と定義する
  - 各要素単体でも部分列なので、初期値をすべて 1 にする
  - 後ろから順に各 index i を処理する
  - i より右側の要素 j を見て、nums[i] < nums[j] なら連結可能
  - 連結できる場合、LIS[i] = max(LIS[i], 1 + LIS[j]) で更新する
  - 最後に LIS 配列の最大値を返す

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(nums) - 1, i, -1):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)
```

時間計算量: $O(n^2)$

空間計算量: $O(n)$
