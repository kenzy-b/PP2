def temperature(F):
    C = (5 / 9) * (F - 32)
    return C

F = float(input("Fahrenheit: "))
C = temperature(F)
print(f"{F} Fahrenheit = {C} Centigrade")



def palindrom(text):
    if text==text[::-1]:
        print("YES")
    else:
        print("NO")

text = input("text: ")
palindrom(text)