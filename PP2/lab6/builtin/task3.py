def reverse(word):
    return word[::-1]


word = "qazaq"
reversed = reverse(word)
if word == reversed:
    print("palindrome")
else:
    print("not palindrome")
