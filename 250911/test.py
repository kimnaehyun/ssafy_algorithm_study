from collections import deque

N, M, V = map(int, input().split())
matrix = [[0] * (N + 1) for _ in range(N + 1)]
used = [0] * (N + 1)

for _ in range(M):
    y, x = map(int, input().split())
    matrix[y][x] = 1
    matrix[x][y] = 1   

def dfs(v):
    used[v] = 1
    print(v, end=' ')
    for i in range(1, N + 1):
        if matrix[v][i] == 1 and not used[i]:
            dfs(i)

def bfs(v):
    q = deque([v])
    visited = [0] * (N + 1)
    visited[v] = 1

    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in range(1, N + 1):
            if matrix[now][i] == 1 and not visited[i]:
                q.append(i)
                visited[i] = 1

dfs(V)
print()
bfs(V)
