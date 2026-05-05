# Step 3

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit += max(prices[i] - prices[i - 1], 0)
        return max_profit
```
1回目: 0分　56秒

2回目: 0分　48秒

3回目: 0　53秒
