import string

Test = input()

for i in range(int(Test)):
    N, S= input().split()
    for cha in S:
        for i in range(int(N)):
            print(cha, end="")
    print()
