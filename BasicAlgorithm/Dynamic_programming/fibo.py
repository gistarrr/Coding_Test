# 다이나믹 프로그래밍을 사용할 수 있는 경우
# 1. 큰 문제를 작은 문제로 나눌 수 있다.
# 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.



d = [0]*100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    
    # 이미 계산한 적이 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))