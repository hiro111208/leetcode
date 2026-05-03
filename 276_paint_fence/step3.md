# Step 3

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
        num_ways_prev_2 = k
        num_ways_prev_1 = k * k

        for i in range(2, n):
            tmp = num_ways_prev_1
            num_ways_prev_1 = (k - 1) * (num_ways_prev_1 + num_ways_prev_2)
            num_ways_prev_2 = tmp
        return num_ways_prev_1
```

1回目: 1分　17秒

2回目: 1分　20秒

3回目: 1分　16秒
