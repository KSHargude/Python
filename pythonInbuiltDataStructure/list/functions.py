#len()
print("1.len()")
l=[10,20,"csd",10.5]
n=len(l)
print(n)  #4
print(len(l))    #4

#count()
print("2.count()")
l=[10,20,"csd",20,20]
l.count(20)
print(l.count(20))     #3
print(l.count("csd"))   #1
print(l.count(10))      #1

print("wihout using count()")
l=[10,20,"csd",20,20]
count=0
for ele in l:
    if ele==20:
        count=count+1
    print(count)

#index()
print("3.index()")
l=[10,20,"csd",20,20]
print(l.index("csd"))   #2
print(l.index(10))    #0
print(l.index(20))    #1    1st occrance

print("without using index()")
def my_index(list,ele):
    index=0
    for e in list:
        if e==ele:
            return index
        index=index+1
    return "element not found"
l=[10,20,"csd",20,20]
my_index(l,10)
print(my_index)          #1
print(my_index(l,40))      #element not found