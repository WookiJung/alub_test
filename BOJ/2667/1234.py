/*
* 메모리: 32124 KB, 시간: 96 ms
* 타이머 시간: null
* 2021.11.17
* by Alub
**/
from collections import deque


def bfs(r,c,group:list):
    queue = deque()
    direction = [(0,1),(1,0),(0,-1),(-1,0)]
    visited[r][c] = 1
    queue.append((r,c))
    group.append((r,c))
    while queue:
        r, c = queue.popleft()
        for k in range(4):
            dr = r + direction[k][0]
            dc = c + direction[k][1]
            if 0 <= dr < N and 0 <= dc < N:
                if not visited[dr][dc] and apt[dr][dc] == '1':
                    queue.append((dr,dc))
                    visited[dr][dc] = 1
                    group.append((dr,dc))
    result.append(len(group))


N = int(input())
apt = [str(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
result = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and apt[i][j] == '1':
            bfs(i,j,[])

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])