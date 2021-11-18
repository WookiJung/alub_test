```
 메모리: 29200 KB, 시간: 80 ms
 풀이 시간: 00:00:21
 2021.11.18
 by Alub
```
N = int(input())

stairs = [int(input()) for _ in range(N)]


dp = [0] * 300
dp[0] = stairs[0]
if N >= 2:
    dp[1] = stairs[0] + stairs[1]
if N >= 3:
    dp[2] = max(stairs[0] + stairs[2],stairs[1]+ stairs[2])
if N >=4:
    idx = 3
    while idx < N:
        dp[idx] = max(dp[idx-3] + stairs[idx-1]+stairs[idx], dp[idx-2] + stairs[idx])
        idx += 1

print(dp[N-1])
