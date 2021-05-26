T = int(input())

for i in range(T):
    x, y = map(int, input().split())

    count = 0
    count_add = 0
    space = 0
    center = (y-x)//2
    i = 1
    start = x

    while(True):
        if start + i <= x + center:
            start += i
            i+=1
            count +=1
            space = start
        elif space + i < x + center + i/2:
            count_add+=2
            break
        elif space + i >= x + center + i/2:
            count_add+=1
            break
    count = count * 2 + count_add
    if (y-x) % 2 == 0:
        print(count)
    else:
        print(count+1)