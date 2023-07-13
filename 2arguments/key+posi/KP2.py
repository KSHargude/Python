def add(num1,num2,num3):
    print(num1+num2+num3)

add(10,20,30)
add(num1=10,num2=20,num3=30)
add(10,num3=10,num2=30)



"""
 add(10,20,30)
add(num1=10,num2=20,num3=30)
add(10,num3=10,num2=30)
add(10,num2=20,30)        add(10,num2=20,30) SyntaxError: positional argument follows keyword argument 



add(10,20,30)
add(num1=10,num2=20,num3=30)
add(10,num3=10,num2=30)
add(10,20,30,40)            

60
60
50
add(10,20,30,40)
TypeError: add() takes 3 positional arguments but 4 were given 



add(num1=10,num2=40,num3=80,num4=40)
add(10,num2=30,num3=30,num4=40)
add(10,num2=20,num3=40) #correct
add(10,num2=20,num1=40)

TypeError
"""