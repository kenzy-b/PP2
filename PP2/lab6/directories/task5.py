f = open("text.txt", "w")
li = input("Input a list of values separated by commas: ").split(", ")
f.write(str(li))
f.close()