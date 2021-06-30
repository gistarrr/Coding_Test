# 최종 순위(백준 3665번)
from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)
    rank = list(map(int, input().split()))
    for i in range(1, len(rank)+1):
        for j in range(1, i):
            graph[rank[i-1]].append(rank[j-1])
            indegree[rank[j-1]] +=1

    m = int(input())
    flag = False
    for i in range(m):
        a, b = map(int, input().split())
        if b in graph[a]:
            graph[b].append(a)
            graph[a].remove(b)
            indegree[b] -= 1
            indegree[a] += 1
        else :
            graph[b].remove(a)
            graph[a].append(b)
            indegree[a] -= 1
            indegree[b] += 1
        
    q = deque()
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)

    result = []

    while q :
        if len(q) == 1:
            now = q.popleft()
            for i in graph[now]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
            result.append(now)
        else :
            flag = True
    if flag or len(result) < n:
        print('IMPOSSIBLE')
    else :
        print(" ".join(list(map(str, result[::-1]))))