import math

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

# 6. 원 찍기
radius = 5
for y in range((radius * 2) + 1):
    for x in range((radius * 2) + 1):
        # 원의 방정식: (x - r)^2 + (y - r)^2 = r^2
        if (x - radius) ** 2 + (y - radius) ** 2 <= radius ** 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# 7. 알파벳 'C' 출력
height = 7
width = 5
for i in range(height):
    if (i == 0 or i == height - 1):
        print('*' * width)  # 'C'의 위쪽과 아래쪽
    elif (i < height - 1):
        print('*')  # 'C'의 왼쪽 부분