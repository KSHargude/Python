class engine:
    def start(self):
        print("engine start")

class car:
    def engine_use(self):
        e=engine()
        e.start()

c=car()
c.engine_use()