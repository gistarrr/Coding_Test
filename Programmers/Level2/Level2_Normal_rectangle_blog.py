def solution(w,h):
    answer = 0
    
    answer = w*h - (w+h-gcd(w,h))
    
    return answer

def gcd(a,b):
    a, b = max(a,b), min(a,b)
    if a % b == 0:
        return b
    else:
        a, b = b, a%b
        return gcd(a, b)