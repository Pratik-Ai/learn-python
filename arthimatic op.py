#calculator

print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

a = int(input("Enter A:"))
b = int(input("Enter B:"))

# input choice
ch=int(input("Enter Choice(1-4): "))

if ch==1:
    c=a+b
    print("Sum = ",c)
elif ch==2:
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    c=a*b
    print("Product = ",c)
elif ch==4:
    c=a/b
    print("Quotient = ",c)
else:
    print("Invalid Choice")
