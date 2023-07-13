#child class constructor called parent class
#  constructor by using super()

class parent:
    def __init__(self):
        print("parent constructor")

class child(parent):
    def __init__(self):
        super().__init__()
        print("child constructor")

c=child()