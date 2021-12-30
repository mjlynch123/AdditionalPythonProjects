# This project takes a string and see if it is a palindrome meaning its the same word backwards like mom or dad
word = input("Enter a word please: ")
backwards_word = ""

for words in reversed(word):
    backwards_word += words

if backwards_word.lower() == word.lower():
    print("This is a palindrome")
else:
    print("This is not a palindrome.")