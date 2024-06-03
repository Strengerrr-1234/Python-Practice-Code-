w = "Welcome {} to {} storage".format("back",40);
print(w)

w = "Welcome {1} to {0} technical".format("Hello",20);      #index number passing through print their number and character
print(w)

# w = "Welcome {a} to {b} technical".format(a = 30,b = 40);
# print(w)

# character shifting their word length and shifting parameter by their length

w = "Welcome {b:10} to {a} technical".format(a = 30,b = 40)            #--------10
print(w)
w = "Welcome {b:^10} to {a} technical".format(a = 30,b = 40)           #----10----  using(^) chracter shifting by their length according to my way
print(w)
w = "Welcome {b:<10} to {a} technical".format(a = 30,b = 40)           #10--------  using(<)
print(w)
w = "Welcome {b:>10} to {a} technical".format(a = 30,b = 40)           #--------10  using(>)
print(w)