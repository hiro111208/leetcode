# Step 1

- 変数を以下の通りにする
  - stockを買う日: `buy_day`
  - その日の値段: `price[buy_day]`
  - 最大利益: `max_profit`
- forループを回していく中で、`price[i]`が`price[buy_day]`より安い場合は`price[buy_day]`を`price[i]`に更新する。高い場合は`max_profit`を更新する

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_day = 0

        for i, price in enumerate(prices):
            if price < prices[buy_day]:
                buy_day = i
            else:
                max_profit = max(max_profit, price - prices[buy_day])

        return max_profit
```

時間計算量: O(n)

空間計算量: O(1)
