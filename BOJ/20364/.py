/*
* 메모리: 140340 KB, 시간: 352 ms
* 타이머 시간: 00:03:50
* 2021.11.18
* by Alub
**/
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
visited = [0] * (N+1)

for i in range(Q):
    x = int(input())
    duck = x
    found = True
    while x > 0:
        if visited[x]:
            last_owned = x
            found = False
        x //= 2
    if found:
        visited[duck] = 1
        print(0)
    else:
        print(last_owned)
