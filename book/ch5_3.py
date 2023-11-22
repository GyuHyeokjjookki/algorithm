import sys
si = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

N, M = map(int,input().split())

print(N, M)
graph = []

for i in range(N):
    graph.append(list(map(int,input())))

def dfs(x, y):
    if x <= -1 or x>= N and y <= -1 or y >= M:\
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if(dfs(i, j) == True):
            result += 1
print(result)