#4Q: Write a program to check if the given number is a palindrome number.
i = int(input("ENTER A NUMBER: "))
rev = 0
check = i
while i >0:
    rev =(rev *10)+ i % 10 
    i = i //10
if (check == rev):
    print("TRUE")
else:
    print("FALSE")
    
