# Step 1

- emailを@で区切る
- @の前から'.'を取り除く
- @の前を'+'で区切る
- @の前と@の後ろをタプルにしてsetに入れる
- setの要素数を返す

```python
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            local_name, domain_name = email.split("@")
            cleansed_local_name = local_name.replace(".", "").split("+")[0]
            res.add((cleansed_local_name, domain_name))
        return len(res)
```

時間計算量: O(n \* m)

空間計算量: O(n)
