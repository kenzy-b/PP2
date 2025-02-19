def trapezoid(height, val1, val2):
    return 0.5 * (val1 + val2)* height

height = int(input())
val1 = int(input())
val2 = int(input())

print(trapezoid(height, val1, val2))