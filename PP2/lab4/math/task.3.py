import math

def polygon(num, length):
    return (num * math.pow(length,2))/ (4 * math.tan(math.pi / num))

num = int(input())
length = int(input())

print(polygon(num, length))