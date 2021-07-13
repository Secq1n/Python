import math


n = int(input())

monkey = []

for i in range(n):
    monkey.append(i+1)

count = 1

temp_n = n

index = 0

while temp_n != 1:
    mokey[index%temp_n] = count
