
# 1. 기본 직각삼각형
n = 5
for i in range(n):
    print('*' * (i + 1))

# 2. 역직각삼각형
for i in range(n):
    print('*' * (n - i))

# 3. 피라미드
for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# 4. 역피라미드
for i in range(n):
    print(' ' * i + '*' * (2 * (n - i) - 1))

# 5. 마름모
n = 3
for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))
for i in range(n-2, -1, -1):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))
