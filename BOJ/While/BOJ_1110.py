import sys

A = int(sys.stdin.readline())
C = A
count=0
while True:
    B = C//10 + C%10 
    C = int(str(C%10) + str(B%10))
    count+=1
    if A == C:
        print(count)
        break  
    
