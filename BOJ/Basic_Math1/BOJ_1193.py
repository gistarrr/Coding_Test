A = int(input())
n = 1 
while n*(n+1)/2 < A:
    n+=1
A = int(A - n*(n-1)/2)
if n % 2 == 1:
    print(str(n-(A-1))+"/"+str(A))
else :
    print(str(A)+'/'+str(n-(A-1)))