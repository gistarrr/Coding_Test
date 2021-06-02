while True:
    triangle = list(map(int, input().split()))
    triangle.sort()
    if triangle[0] == 0 and triangle[1] == 0 and triangle[2] == 0 :
        break
    if triangle[2]**2 == triangle[1]**2 + triangle[0]**2:
        print("right")
    else :
        print("wrong")
