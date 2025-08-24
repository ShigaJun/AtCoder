import math

N = int(input())
x = list(map(int, input().split()))
abs_x = [abs(xi) for xi in x]
pow_x = [math.pow(xi, 2) for xi in x]

print(sum(abs_x))
print(math.sqrt(sum(pow_x)))
print(max(abs_x))