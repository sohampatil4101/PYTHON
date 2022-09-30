n = int(input("Enter the number of rows in pattern \n"))
i=0
for rows in range(0,n,1):
    i=i+1
    for star in range(0,i,1):
        print("*", end="")
    print("\n")
    if i ==n: break

