def draw_shapes():
    print("1. 피라미드 별찍기")
    for i in range(5):
        print(" " * (4-i) + "*" * (2*i+1))
    print()
    
    print("2. 사각형 그리기")
    for i in range(5):
        if i == 0 or i == 4:
            print("* " * 5)
        else:
            print("*       *")
    print()
    
    print("3. 하트 모양")
    for i in range(6):
        if i == 0:
            print("  *   *  ")
        elif i == 1:
            print("* * * * *")
        elif i == 2:
            print("* * * * *")
        else:
            print(" " * i + "*" * (9-2*i))
    print()

if __name__ == "__main__":
    draw_shapes()
