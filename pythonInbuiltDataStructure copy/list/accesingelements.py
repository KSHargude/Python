#by using index
#by using slice operator
l=[10,20,30,'csd',10.5]
print(l)
print(l[2])    #30
print(l[-3])   #30
print(l[1:4])   #[20,30,"csd"]
print(l[1:4:2])       #[20,"csd"]
print(l[4:1:-1])       #[10.5,"csd",30]
print(l[4:1:-2])      #[10.5,30]
print(l[1:2:-1])    #[]
print(l[-2:-3])
print(l[1:2:-1])
print(l[::])    #al elements
print(l[:4])
print(l[::-1])