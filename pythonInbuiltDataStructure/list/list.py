#preservation, duplicate data, indexing
l=[10,20,30,"csd",10.5]
print(type(l))
print(l)
print("---------------------")
#duplicate
l=[10,20,30,"csd",10.5,10,20]
print(l)
print(type(l))
print("---------------------")
#indexing
print(l[3])
print(l[-2])
print(l)
print("---------------------")
#mutable
l[2]=200
l[1]=100
print(l)
print("-----------------------")
#creation of list obj
# 1.empty list
l=[]
print(type(l))
print(l)
print("-------------------")
# 2.list with content
# 3.taking dynamic input
l=eval(input("Enter number: "))
print(type(l))
print(l)
print("---------------------")
i=input("Enter list: ")
print(type(l))
print(l)
print("----------------------")
# 4.next page
