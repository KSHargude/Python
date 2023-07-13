      #1
# class parent:
#     def property(self):
#         print("gold+cash+power")
#     def marry(self):
#         print("abc")

# class child(parent):
#     def marry(self):
#         print("pqr")

# c=child()
# c.property()         #gold+cash+power
# c.marry()            #pqr


       #2
# class parent:
#     def property(self):
#         print("gold+cash+power")
#     def marry(self):
#         print("abc")

# class child(parent):
#     def marry(self):
#         super().marry()
#         print("pqr")

# c=child()
# c.property()          #gold+cash+power
# c.marry()             #abc          
#                       #pqr



         #3
class parent:
    def property(self):
        print("gold+cash+power")
    def marry(self):
        print("abc")

class child(parent):
    def marry(self):
        super().marry()
        print("pqr")
        self.property()
        super().property()
        parent.property(10)
        print("xyz")

c=child()
c.property()         
c.marry()     