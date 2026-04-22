# Step 2

```python
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local_name, domain_name = email.split("@")
            cleansed_local_name = local_name.replace(".", "").split("+")[0]
            unique_emails.add((cleansed_local_name, domain_name))
        return len(unique_emails)
```
