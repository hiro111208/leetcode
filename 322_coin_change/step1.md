# Step 1

- 部分問題を解く
  - base case: amountが0のときに必要なコインの枚数は0
  - $dp[amount]=min(dp[amount], 1 + dp[amount - coin])$
  - amountにするのに必要な最小のコインの枚数は、amountからコインを引いた分にするのに必要な最小のコインの枚数に1を足したものである

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[amount] if dp[amount] != float('inf') else -1
```

時間計算量: $O(nm)$

空間計算量: $O(m)$

$n$: $coins$のサイズ

$m$: $amount$の大きさ
