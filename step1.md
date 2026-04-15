# Step 1

1. Counter()を使用した解法を思いついた。しかし、ライブラリの使い方を忘れたため、ドキュメントを読んだ。

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_counter = Counter(nums)
        return [element for element, _ in element_counter.most_common(k)]
```

2. Heapの問題なので、それを使った解法を考えた。

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 各数字が現れる回数を数える
        element_counter = {}
        for num in nums:
            element_counter[num] = 1 + element_counter.get(num, 0)

        # 最小ヒープを使って最も多く現れる数字k個を格納
        heap = []
        for key, value in element_counter.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)

        # ヒープから出力に合うよう結果を整形
        res = []
        for _, key in heap:
            res.append(key)

        return res
```
