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