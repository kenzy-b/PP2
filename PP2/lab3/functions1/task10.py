def unique(list):
    result = []
    for i in list:
        if list.count(i) == 1:
            result.append(i)
    return result

n = int(input("Numbers of element: "))
list = []
for i in range(n):
    number = int(input("Number: "))
    list.append(number)
print(unique(list))