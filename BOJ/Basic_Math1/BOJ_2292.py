A = int(input())
room = 1
k = 1
while A > room:
    room += 6*k
    k+=1
print(k)