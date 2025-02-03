def reversing(strings):
    strings=list(strings.split())
    strings.reverse()
    for i in strings:
        print(i, end=" ")

k=str(input("Enter sentence: "))
reversing(k)