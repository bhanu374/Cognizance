# 2Q:Write a program to accept a string from the user and display characters, that are present at an even index number.
str = input("ENTER A STRING: ")
index = 0

while (index < len(str)):
    print(str[index],end = "")
    index = index + 2
    