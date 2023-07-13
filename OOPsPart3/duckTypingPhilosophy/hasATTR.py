class duck:
    def speak(self):
        print("quack....quack")

class dog:
    def bark(self):
        print("bow....bow")

class cat:
    def speak(self):
        print("meow.....meow")


def f1(obj):
    if hasattr(obj,'speak'):
        obj.speak()
    else:
        obj.bark()

d=duck()
f1(d)
d1=dog()
f1(d1)
c=cat()
f1(c)

