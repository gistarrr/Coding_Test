import string

S = input()

for alpha in string.ascii_lowercase:
    print(S.find(alpha), end=" ")