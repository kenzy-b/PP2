with open("text.txt", "r") as f1:
    f2 = open(f"copy_text.txt", "w")
    for line in f1:
        f2.write(line)
    f1.close()