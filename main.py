import math

n = 5

# 피라미드 형태
for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# 역 피라미드 형태
for i in range(n - 2, -1, -1):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))
for i in range(n - 2, -1, -1):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# 기본 피라미드 예제
print("\n기본 피라미드:")
for i in range(n):
    print(' ' * (n - i - 1) + '*' * (i + 1))

# 역 피라미드 예제
print("\n역 피라미드:")
for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * i)

# 다이아몬드 형태
print("\n다이아몬드:")
for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))
for i in range(n - 2, -1, -1):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# 직각삼각형 형태
print("\n직각삼각형:")
for i in range(1, n + 1):
    print('*' * i)

# 원 형태
print("\n원:")
radius = n // 2
for y in range(-radius, radius + 1):
    for x in range(-radius, radius + 1):
        if math.isclose(x**2 + y**2, radius**2, abs_tol=0.5):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()