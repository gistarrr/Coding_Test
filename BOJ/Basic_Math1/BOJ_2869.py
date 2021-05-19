import math

input_data = list(map(int, input().split()))

days = math.ceil((input_data[2]-input_data[0]) / (input_data[0] - input_data[1])) + 1

print(days)