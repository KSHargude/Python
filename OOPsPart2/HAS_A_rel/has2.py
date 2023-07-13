class engine:
    def start (self):
        print("engine start")

class car:
    def __init__(self,color,model,en):
        self.color=color
        self.model=model
        self.en=en

    def engine_use(self):
        print(self.color)
        print(self.model)
        self.en.start()
        print("engine used successfully")

e=engine()
c=car("black","kg56",e)
c.engine_use()