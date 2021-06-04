# # 이진 탐색
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start+mid)//2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else :
#             start = mid + 1
#     return None

# N = int(input())
# N_list = list(map(int, input().split()))
# N_list.sort()

# M = int(input())
# M_list = list(map(int, input().split()))

# for i in M_list:
#     result = binary_search(N_list, i, 0, len(N_list)-1)
#     if result == None:
#         print("no", end=" ")
#     else:
#         print("yes", end=" ")

# 계수 정렬
n = int(input())
array = [0]*1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    if array[i] == 1:
        print("yes", end=' ')
    else :
        print("no", end=' ')
