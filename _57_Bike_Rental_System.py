class bikeshop:

    def __init__(self,stock):
        self.stock= stock
    def displayBike(self):
        print("Total Bikes",self.stock)
    def renForBike(self,q):

        if q<=0:
             print("Enter th Positive Value or greater than zero")
        if q>self.stock:
            print("Enter the value less than stock")
        else:
            print("Total Prices",q*100 )
            print("Total Bikes ",self.stock)

while True:
    obj = bikeshop(100)
    uc = int(input('''
       1. Display Stocks 
       2. Rent a Bike 
       3. Exit
    '''))

    if uc==1:
        obj.displayBike()
    elif uc==2:
        n = int(input("Enter the Qty "))
        obj.rentForBike(n)
    else:
        break