def Cal(a, b):
    person = 0
    simplify = []
    if a == 0:
        return b
    else:
        for i in range(1, b+1):
            person += Cal(a-1,i)
        return person

result = []

Test_cast = int(input())

for i in range(Test_cast):
    k = int(input())
    n = int(input())
    result.append(Cal(k,n))

for i in result:
    print(i)

# T = int(input())

# for _ in range(T):
#     k = int(input())
#     n = int(input())
#     people = [ i for i in range(1, n+1)]
#     for __ in range(k):
#         for j in range(1,n):
#             people[j] += people[j-1]
#     print(people[-1])