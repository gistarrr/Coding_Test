number = input()
time = 0
alpha = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

for i in number:
    for j in alpha:
        if i in j:
            time+=alpha.index(j)+3
print(time)