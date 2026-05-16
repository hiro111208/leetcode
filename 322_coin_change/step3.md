# Step 3

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [float('inf')] * (amount + 1)
        min_coins[0] = 0

        for sub_amount in range(1, amount + 1):
            for coin in coins:
                if sub_amount - coin >= 0:
                    min_coins[sub_amount] = min(min_coins[sub_amount], 1 + min_coins[sub_amount - coin])

        return min_coins[amount] if min_coins[amount] != float('inf') else -1
```

1回目: 2分　48秒

2回目: 2分　41秒

3回目: 1分　49秒
