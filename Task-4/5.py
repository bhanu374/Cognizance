#5Q:Print the following pattern
n = int(input("ENTER NUMBER OF ROWS:"))
for x in range (n) :
    for y in range(n-x-1) :
        print(" ",end="")
    for y  in range(x+1):
        print("*",end=" ")
    print()