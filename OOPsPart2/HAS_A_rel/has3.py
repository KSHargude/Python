class engine:
    def __init__ (self,model):
        self.model=model
    def engine_info(self):
        print(f"engine with{self.model}number")

class car:
    def __init__(self,color,model,en):
        self.color=color
        self.model=model
        self.en=en

    def engine_use(self):
        print(self.color)
        print(self.model)
        print(self.en.model)
        self.en.engine_info()
        print("engine used successfully")

e=engine("fds20")
c=car("black","kg56",e)
c.engine_use()