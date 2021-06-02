import math

T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = math.sqrt(math.pow(abs(x1-x2),2) + math.pow(abs(y1-y2), 2))
    r_max = max(r1, r2)
    r_min = min(r1, r2)

    if distance == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if distance < r_max :
            if distance + r_min < r_max:
                print(0)
            elif distance + r_min == r_max:
                print(1)
            else :
                print(2)
        elif distance == r_max:
            print(2)
        else:
            if distance == r_min + r_max:
                print(1)
            elif distance <= r_min + r_max:
                print(2)
            else :
                print(0)