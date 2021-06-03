import copy

N = int(input())

RGB = [list(map(int, input().split())) for _ in range(N)]

first_sum = RGB[0][0]
second_sum = RGB[0][1]
third_sum = RGB[0][2]

fir_pra = copy.deepcopy(RGB)
sen_pra = copy.deepcopy(RGB)
trd_pra = copy.deepcopy(RGB)

fir_pra[1][0] += 1000
sen_pra[1][1] += 1000
trd_pra[1][2] += 1000

for i in range(1, len(RGB)-1):
    first_sum += min(fir_pra[i])
    fir_pra[i+1][fir_pra[i].index(min(fir_pra[i]))] += 1000
first_sum += min(fir_pra[N-1])

for i in range(1, len(RGB)-1):
    second_sum += min(sen_pra[i])
    del sen_pra[i+1][sen_pra[i].index(min(sen_pra[i]))]
second_sum += min(sen_pra[N-1])

for i in range(1, len(RGB)-1):
    third_sum += min(trd_pra[i])
    del trd_pra[i+1][trd_pra[i].index(min(trd_pra[i]))]
third_sum += min(trd_pra[N-1])

print(min(first_sum, second_sum, third_sum))