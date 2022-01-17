n = int(input())

check ='666'
num = 666
count = 0
while True :
    if '666' in str(num):
        count += 1
        if count == n :
            print(num)
            break
        else :
            num += 1
    else :
        num += 1