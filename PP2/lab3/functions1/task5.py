def permutations(word):
    n = len(word)

    for i in range(n):
        for j in range(n):
            print(word[(j-i)], end="")
        print()
k=str(input("enter word: "))
permutations(k)