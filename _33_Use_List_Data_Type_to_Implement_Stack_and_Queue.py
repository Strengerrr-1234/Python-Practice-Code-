# Stack implement
# l =[]
# while True:
#     c=int(input('''
#         1 Push Element
#         2 Pop  Element
#         3 Peek Element
#         4 Display Stack
#         5 Exit
#       '''))
#     if c==1:
#         n = input("Enter The value");
#         l.append(n)
#         print(l)
#     elif c==2:
#         if len(l)==0:
#             print("Empty Stack")
#         else:
#             p = l.pop()
#             print(p)
#             print(l)
#     elif c==3:
#         if len(l)==0:
#             print("Empty Stack")
#         else:
#             print("Last Stack Value",l[-1])
#     elif c==4:
#         print("Display Stack",l)
#     elif c==5:
#         break;
#     else:
#         print("Invalid Operation")


# Queue 
l =[]
while True:
    c=int(input(''' 
        1 Push Element
        2 Pop  First Element
        3 Front Element
        4 Last Element
        5 Display Stac
        6 Exit
        
      '''))
    if c==1:
        n = input("Enter The value");
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty Queue")
        else:
            del l[0]
            print(p)
            print(l)
    elif c==3:
        if len(l)==0:
            print("Empty Queue")
        else:
            print("First Queue Value",l[0])
    elif c==4:
        if len(l)==0:
            print("Empty Queue")
        else:
            print("Last Queue Value ",l[-1])
    elif c==5:
        print("Display Queue")
    elif c==6:
        break;
    else:
        print("Invalid Operation...")



