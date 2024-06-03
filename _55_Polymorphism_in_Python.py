class Ws:
    def displayinfo(self):
        print("Welcome to wscubetech")

class IIP(Ws):
    def displayinfo(self):
        super().displayinfo()
        print("Welcome to IIP")

obj = IIP()
obj.displayinfo()






# class Ws:
#     def displayinfo(self,name=''):
#         print("Welcome to Wscubtech"+name)
#
# obj = Ws()
# obj.displayinfo()
# obj.displayinfo(' python')