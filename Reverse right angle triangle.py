n = int(input("Enter the number of rows in pattern \n"))
i=n+1
for rows in range(0,n,1):
    i=i-1
    for star in range(0,i,1):
        print("*", end="")
    print("\n")
    # if i ==: break

