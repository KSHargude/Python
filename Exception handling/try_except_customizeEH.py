n1=int(input("enter first number: "))
n2=int(input("enter 2nd number: "))
try:
    print(n1/n2)
except ZeroDivisionError:
    print(n1/1)
print("end")