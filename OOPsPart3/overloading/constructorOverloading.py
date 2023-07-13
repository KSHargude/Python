#not supported

# class test:
#     def __init__(self,a,b):
#         print(a+b)
#     def __init__(self,a,b,c):
#         print(a+b+c)
# t=test(1,2,3)     #6
# t=test(1,2)       #error    bcoz 2nd override 1st constructor


#default

# class test:
#     def __init__(self,a=0,b=0,c=0):
#         print("1")
#     def __init__(self,a=0,b=0):
#         print("2")
# t=test(10,20)        #2
# t=test(10,20,30)     # error


#ver length

class test:
    def __init__(self,*n):
        sum=0
        for ele in n:
            sum=ele+sum
        print(sum)
t=test(1,3,4,5,6)     #19
