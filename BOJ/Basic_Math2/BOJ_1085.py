x, y, w, h = map(int, input().split())

dis = min(abs(w-x), abs(h-y), abs(x), abs(y))

print(dis)