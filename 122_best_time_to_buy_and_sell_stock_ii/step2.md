# Step 2

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

時間計算量: $O(n)$

空間計算量: $O(1)$
