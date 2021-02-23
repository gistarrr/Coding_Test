def d(n):
    a=0
    for i in str(n):
        a+=int(i)
    a+=n
    return a

num = set(range(1, 10000+1))
Nself_num=set()
for i in num:
    Nself_num.add(d(i))
self_num = num - Nself_num
for i in sorted(self_num):
    print(i)