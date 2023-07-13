class duck:
    def speak(self):
        print("quack.....quack")

class dog:
    def speak(self):
        print("bow....bow")

class cat:
    def speak(self):
        print("meow....meow")

def f1(obj):
    obj.speak()

d=duck()
f1(d)
d1=dog()
f1(d1)
c=cat()
f1(c)