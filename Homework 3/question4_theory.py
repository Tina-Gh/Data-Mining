import math

x = 0
sum = 0
e = 0.35

for i in range(13, 26):
    x = math.factorial(25) / (math.factorial(i) * math.factorial(25-i)) * pow(e, i) * pow((1-e), (25-i))
    sum += x

print(sum)