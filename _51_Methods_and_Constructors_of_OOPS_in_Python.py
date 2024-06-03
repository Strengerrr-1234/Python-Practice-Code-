class DemoClass:
    a = 10
    def showvalue(self):
        self.c = self.a*self.a
        print(self.c)

    def showvalue1(self):
        print("Welcome to myway")


    def __init__(self):        # create constructor
        print("My Office")


obj=DemoClass()
obj.showvalue()
obj.showvalue1()