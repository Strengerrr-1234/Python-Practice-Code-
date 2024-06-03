import random
n = random.randint(2,8)
print(n)

n1 = random.randrange(2,4)
print(n1)

l = [10,20,30,40]
lc = random.choice(l)
print(lc)

# random()     Returns a random float number between 0 and 1
# shuffle()    Takes a sequence and returns the sequence in a random ordered_set
# uniform()    Returns a random float number between two given parameter

r = random.random()
print(r)

l = [10,20,30,40]
random.shuffle(l)
print(l)

u = random.uniform(3,9)
print(u)

