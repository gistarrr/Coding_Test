Weight = int(input())

answer = 0
flag = False
if Weight % 5 == 0:
    print(int(Weight/5))
else:
    for i in range(Weight//5, -1, -1):
        if (Weight - i*5) % 3 == 0:
            print(i+(Weight - i*5) // 3)
            flag = True
            break
    if(flag == False):
        print(-1)