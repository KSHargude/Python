       #1
# class parent:
#     def __init__(self):
#         print("PC")
# class child(parent):
#     pass
# c=child()       #PC



        #2
# class parent:
#     def __init__(self):
#         print("PC")
# class child(parent):
#     def __init__(self):
#         print("CC")
# c=child()            #CC



        #3
class parent:
    def __init__(self):
        print("PC")
class child(parent):
    def __init__(self):
        print("CC")
        super().__init__()
c=child()            