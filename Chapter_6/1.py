# Write a program that asks the user to enter a string. The program should then print the
# following:
# (a) The total number of characters in the string
# (b) The string repeated 10 times
# (c) The first character of the string (remember that string indices start at 0)
# (d) The first three characters of the string
# (e) The last three characters of the string
# (f) The string backwards
# (g) The seventh character of the string if the string is long enough and a message otherwise
# (h) The string with its first and last characters removed
# (i) The string in all caps
# (j) The string with every a replaced with an e
# (k) The string with every letter replaced by a space

s = input("Enter a string")
l = print("Total number of character in string", len(s))
print(s*10)
print("First cahracter of string ",s[0])
print("First 3 character of string",s[:2])
print("Last 3 character of string",s[::-3])
print("Backward",s[::-1])
if len(s) < 6:
    print("charcater is shot")
else:
    print("seventh character",s[6])
v =''
for i in range(1,len(s)-1):
    v +=s[i]
print(v)
print(s[1:-1])
print(s.capitalize())
print(s.replace('a','e'))
