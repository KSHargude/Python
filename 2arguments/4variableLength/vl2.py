def add(*n):
    result=0

    for ele in n:
        result=result+ele
    print(result)

add(10,20,30,40,50)   # direct 50


"""
def add(*n):
    result=0

    for ele in n:
        result=result+ele
        print(result)

add(10,20,30,40,50)   

10
30
60
100
150 """

