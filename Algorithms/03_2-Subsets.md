```python
# 부분 집합 구하기(조합, Combination)
def dfs(n, ans, i):
    if len(ans) == i:
        print(ans)
        """

        여기서 ans갖고 작업할 수 있을 것!?
        
        """
        return

    if n == len(numbers):
        return

    dfs(n+1, ans+[numbers[n]], i)
    dfs(n+1, ans, i)


numbers = [1, 2, 3, 4]
ans = []
for i in range(len(numbers)+1):
    dfs(0, ans, i)
    print()
```

