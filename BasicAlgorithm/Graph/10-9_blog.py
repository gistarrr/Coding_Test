from collections import deque
import copy
N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
time = [0]*(N+1)

for i in range(1, N+1):
    info = list(map(int, input().split()))
    time[i] = info[0]
    for x in info[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0 :
            q.append(i)

    while q :
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            if indegree[i] == 0 :
                q.append(i)

    for i in range(1, N+1):
        print(result[i])

topology_sort()