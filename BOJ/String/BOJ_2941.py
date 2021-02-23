data = input()
Cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
result = []

for i in range(len(Cro)):
    data = data.replace(Cro[i], 'a')
print(len(data))