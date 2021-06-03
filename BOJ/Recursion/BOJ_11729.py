cnt = 0
string_stack = []

def Hanoi(N, start : str, middle : str, dest : str):
    global cnt
    global string_stack
    if N == 1:
        string_stack.append(f'{start} {dest}')
        cnt += 1
    else:
        Hanoi(N-1, start, dest, middle)
        string_stack.append(f'{start} {dest}')
        cnt += 1
        Hanoi(N-1, middle, start, dest)


N = int(input())

Hanoi(N, 1, 2, 3)
print(cnt)
for i in string_stack:
    print(i)