```
 메모리: 29200 KB, 시간: 76 ms
 2021.11.19
 by Alub
```
memo = []
for i in range(41):
    if i == 0:
        memo.append([1, 0])
    if i == 1:
        memo.append([0, 1])
    if i >= 2:
        memo.append([memo[i-2][0] + memo[i-1][0], memo[i-2][1] + memo[i-1][1]])

T = int(input())
for tc in range(T):
    N = int(input())
    print(memo[N][0], memo[N][1])
