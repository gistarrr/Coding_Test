N = int(input())

create = [0]*N

for i in range(N):
    create[i] = i
    for j in str(i):
        create[i] += int(j)
answer = 0
for i, v in enumerate(create):
    if v == N:
        answer = i
        break;
print(answer)