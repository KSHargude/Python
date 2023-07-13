#do not support


# class test:
#     def add(a,b,c):
#         print(a+b+c)
#     def add(a,b):
#         print(a+b)  
# test.add(10,20)        #30
# test.add(10,20,38)     #error    second add method override the first add method


# class test:
#     def add(a=0,b=0,c=0,d=0):
#         print(a+b+c+d)
# test.add(10)                    #10
# test.add(10,20)                 #30
# test.add(10,20,30)               #60
# test.add(10,20,30,40)            #100
# test.add(1,2,3,4,5)              #error


class test:
    def add(*n):
        sum=0
        for ele in n:
            sum=ele+sum
        print(sum)
test.add(1,2,3,45,6,6,6)

