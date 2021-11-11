/*
* 메모리: 99180 KB, 시간: 2340 ms
* 타이머 시간: null
* 2021.11.11
* by Alub
**/
from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
edges=[[] for _ in range(N+1)]
for m in range(M):
    start, end = map(int, input().split())
    edges[start].append(end)

q= deque()
q.append(X)
count = [-1] * (N+1)
count[X] = 0
while q:
    node = q.popleft()
    for c in edges[node]:
        if count[c] == -1:
            count[c] = count[node] + 1
            q.append(c)

result = False
for i in range(len(count)):
    if count[i] == K:
        result = True
        print(i)

if not result:
    print(-1)
