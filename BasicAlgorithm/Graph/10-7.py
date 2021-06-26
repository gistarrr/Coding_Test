N, M = map(int, input().split())

parent = [0]*(N+1)
for i in range(1, N+1):
    parent[i] = i

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b
    
for i in range(M):
    flag, a, b, = map(int, input().split())
    if not flag:
        union_parent(parent, a, b)
    else :
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print("NO")