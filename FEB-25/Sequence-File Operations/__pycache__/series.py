n= int(input("enter the positive number:"))
if n<0:
    print("Please enter the positive number")
else:
    series= sum( i / (i+1) for i in range(1,n+1))
print (f"sum of series for n{n} is: {series:.6f}")

