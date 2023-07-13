rno=1
name="krutika"
age=20

print("my name is",name,"and age is",age)
print("my name is {} and age is {}".format(name,age))
print("my name is {} and age is {}".format(age,name))
print("my name is {1} and age is {0}".format(age,name))
# print("my name is {1} and age is {}".format(age,name))     gives the error bcoz {}
#imp
print("my name is {y} and age is {x}".format(x=age,y=name))
#f
print(f"my name is {name} and age is {age}")

 # print("my name is" +name+ "and my age is" +age)        gives error string and int cannot concatenate   #type error