# Step 3

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buying_price = prices[0]

        for price in prices:
            buying_price = min(buying_price, price)
            max_profit = max(max_profit, price - buying_price)

        return max_profit
```

1回目: 1分　9秒

2回目: 1分　10秒

3回目: 1分　11秒
