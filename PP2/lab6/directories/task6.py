abc = "abcdefghijklmnopqrstwxyz"

for i in abc:
    with open(f"{i}.txt", 'w') as file:
        file.write(f"This is file {i}")
