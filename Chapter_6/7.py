# . Write a program that asks the user to enter a word and determines whether the word is a
# palindrome or not. A palindrome is a word that reads the same backwards as forwards.

str = input("enter a string")
if (str == str[::-1]):
    print("palindrome")
else:
    print("not palindrome")