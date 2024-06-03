class A:
    def Display_A(self):
        print("Welcome to my Office A")

class B(A):
    def Display_B(self):
        print("Welcome to my office B")

class C(B):
    def Display_C(self):
        print("Welcome to my office C")


obj = C()
obj.Display_A()
obj.Display_B()
obj.Display_C()