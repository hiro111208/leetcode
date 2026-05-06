# Step 1

## 解法1

- 全ペアの和を二重ループで計算する
- k個の最小の和のため、heapを使う
- heapqは最小ヒープ、すなわちpopすると最小の和から出ていくため、和にマイナスをつけることで、最大の和から出ていくようにする

```python
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for num1 in nums1:
            for num2 in nums2:
                if len(heap) == k:
                    heapq.heappushpop(heap, (-(num1 + num2), [num1, num2]))
                else:
                    heapq.heappush(heap, (-(num1 + num2), [num1, num2]))

        res = [pair for _, pair in heap]
        return res
```

- 結果: Time Limit Exceeded
- constraintsに"1 <= nums1.length, nums2.length <= 10^5"とあるのでこの結果になった

## 解法2

- 各整数配列はnon-decreasing orderなので、これを活かしたい。が、思いつかなかったので[ここ](https://algo.monster/liteproblems/373)を参考にした。
  1. 例えば入力がnums1 = [1,7,11], nums2 = [2,4,6], k = 3とする
  2. 2つの配列の値を下記のように配置する

  |       |     |  0  |  1  |  2  |
  | :---: | :-: | :-: | :-: | :-: |
  |       |     |  1  |  7  | 11  |
  | **0** |  2  |     |     |     |
  | **1** |  4  |     |     |     |
  | **2** |  6  |     |     |     |
  3. あるインデックス(i,j)の和の次に最小の和は、(i + 1, j)か(i, j + 1)である

```python
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = [[nums1[i] + nums2[0], i, 0] for i in range(len(nums1))]
        heapq.heapify(min_heap)
        res = []

        while min_heap and k > 0:
            _, index1, index2 = heapq.heappop(min_heap)
            res.append([nums1[index1], nums2[index2]])
            k -= 1

            if index2 + 1 < len(nums2):
                heapq.heappush(min_heap, [nums1[index1] + nums2[index2 + 1], index1, index2 + 1])

        return res
```
