V1, V2, V3 = list(input().split()), list(input().split()), list(input().split())

V4 = []

if V1[0] == V2[0]:
    V4.append(V3[0])
elif V1[0] == V3[0]:
    V4.append(V2[0])
else :
    V4.append(V1[0])

if V1[1] == V2[1]:
    V4.append(V3[1])
elif V1[1] == V3[1]:
    V4.append(V2[1])
else :
    V4.append(V1[1])

print(V4[0], V4[1])