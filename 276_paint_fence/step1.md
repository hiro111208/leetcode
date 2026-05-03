# Step 1

- 3連続同じ色にはできない
- $post_{k}$に塗れる色は、$post_{k - 1}$、$post_{k - 2}$による
- 解けなかったので[解説](https://www.geeksforgeeks.org/dsa/painting-fence-algorithm/)を見た
  - 塗り方の選択肢は2つ
    1. $post_{n}$を$post_{n-1}$と違う色にする
       - 色の選択肢は$k-1$
    2. $post_{n}$と$post_{n-1}$を同じにする
       - 色の選択肢は$k-1$
  - $numWays(n) = numWays(n - 2) * (k - 1) + numWays(n-1)*(k-1)$

```python
class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def num_ways(self, n: int, k: int) -> int:
        # write your code here
        if n == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k * k
        return num_ways(n - 1) * (k - 1) + num_ways(n - 2) * (k - 1)
```

時間計算量: $O(2^n)$

空間計算量:$O(n)$
