def AP(data):
    if data<100:
        return 1
    else : 
        A = list(str(data))
        cal = int(A[0]) - int(A[1])
        for i in range(1, len(A)-1):
            if cal != int(A[i]) - int(A[i+1]) :
                return 0
        return 1

N = int(input())
count=0
for i in range(1, N+1):
    if AP(i) == 1:
        count+=1        
print(count)