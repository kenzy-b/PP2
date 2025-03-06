s = input("enter a string: ")

upper, lower = 0, 0
for c in s:
    if c.isupper:
        upper += 1
    elif c.islower:
        lower += 1

print(f" uppercase letters: {upper}\n lowercase letters: {lower}")