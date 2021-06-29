# 럭키 스트레이트 (백준 18406번)
N = input()
l_sum = sum(map(int, N[:len(N)//2]))
r_sum = sum(map(int, N[len(N)//2:]))
if l_sum == r_sum:
    print("LUCKY")
else :
    print("READY")